from datetime import timedelta
from django.shortcuts import render, redirect, render_to_response
from search_game.models import City, Balance
from search_game.utils import flight_distance, flight_cost, flight_time
from world import settings
from search_game.forms import CreateSearch, FindCity
from random import randint
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, 'home.html')


def success(request):
    return render(request, 'success.html')


def failure(request):
    return render(request, 'failure.html')


def register(request):
    if request.method == 'POST':
        form = CreateSearch(request.POST)
        if form.is_valid():
            form.save()
            current_user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password1'])
            # Code needs a legitimate mailing backend before being implemented
            # current_user.email_user(
            #     'Welcome!',
            #     'Thanks for joining our website.',
            #     settings.DEFAULT_FROM_EMAIL
            # )
            current_city = City.objects.get(name='San Francisco')
            random_city = randint(1, 23)
            Balance.objects.create(
                user=current_user,
                start=current_user.date_joined,
                end=(current_user.date_joined + timedelta(days=14)),
                current_city=current_city.id,
                hidden=random_city,
            )
            # request.user = User.objects.get(id=current_user.id)
            login(request, current_user)
            return redirect(profile)
    else:
        form = CreateSearch()
    return render(request, 'registration/register.html', {'form': form})

@login_required
def profile(request):
    if request.user.balance.money < 0:
        return redirect(failure)
    data = {'city': City.objects.get(id=request.user.balance.current_city)}
    return render(request, 'profile.html', data)


def map(request):
    current_city = City.objects.get(id=request.user.balance.current_city)
    # current.location.current = False
    data = {'current': None, 'destination': None}
    if request.method == 'POST':
        form = FindCity(request.POST)
        if form.is_valid():
            new_city = form.cleaned_data['destination']
            distance = flight_distance(current_city, new_city)
            data = {
                'form': form,
                'current': current_city,
                'destination': new_city,
                'cost': flight_cost(distance),
                'duration': flight_time(distance),
            }
            # request.user.location.city = new_city
            # new_city.location.current = True
    else:
        form = FindCity()
        data = {
            'current': current_city,
            'destination': None,
            'form': form
        }
    return render(request, 'map.html', data)


def city_view(request, city_id):
    
    previous_city = City.objects.get(id=request.user.balance.current_city)
    current_city = City.objects.get(id=city_id)
    distance = flight_distance(previous_city, current_city)
    cost = flight_cost(distance)
    time = flight_time(distance)
    new_start = request.user.balance.start + timedelta(hours=time)

    request.user.balance.arrive(city_id)
    request.user.balance.minus_money(cost)
    request.user.balance.update_time(new_start)
    request.user.balance.save()
    
    if city_id == request.user.balance.hidden:
        request.user.balance.found = True
    data = {'city': current_city}
    return render(request, 'city_view.html', data)
