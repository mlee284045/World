from datetime import timedelta
from django.shortcuts import render, redirect
from search_game.models import City, Balance
from search_game.utils import flight_cost
from world import settings
from search_game.forms import CreateSearch, FindCity
from random import randint


def home(request):
    return render(request, 'home.html')


def register(request):
    if request.method == 'POST':
        form = CreateSearch(request.POST)
        if form.is_valid():
            current_user = form.save()
            # current_user.email_user(
            #     'Welcome!',
            #     'Thanks for joining our website.',
            #     settings.DEFAULT_FROM_EMAIL
            # )
            current_city = City.objects.get(name='San Francisco')
            random_city = randint(1, )
            Balance.objects.create(
                user=current_user,
                start=current_user.date_joined,
                end=(current_user.date_joined + timedelta(days=14)),
                current_city=current_city.id,
            )
            return redirect('profile')
    else:
        form = CreateSearch()
    return render(request, 'registration/register.html', {'form': form})


def profile(request):
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

            data = {
                'form': form,
                'current': current_city,
                'destination': new_city,
                'cost': flight_cost(current_city, new_city)
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
    current_city = City.objects.get(id=city_id)

    request.user.balance.arrive(current_city.id)

    if current_city == request.user.hidden:
        request.user.balance.found = True
    data = {'city': current_city}
    return render(request, 'city_view.html', data)
