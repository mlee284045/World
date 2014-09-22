from datetime import timedelta
from django.shortcuts import render, redirect
from search_game.models import City, Balance
from search_game.utils import hiding_person
from world import settings
from search_game.forms import CreateSearch, FindCity

# Create your views here.


def home(request):
    return render(request, 'home.html')


def register(request):
    if request.method == 'POST':
        form = CreateSearch(request.POST)
        if form.is_valid():
            current_user = form.save()
            current_user.email_user('Welcome!', 'Thanks for joining our website.', settings.DEFAULT_FROM_EMAIL)
            Balance.objects.create(user=current_user, start=current_user.date_joined, end=(current_user.date_joined+timedelta(days=14)))

            return redirect('profile')
    else:
        form = CreateSearch()
    return render(request, 'registration/register.html', {'form': form})


def profile(request):
    return render(request, 'profile.html')


def map(request):
    rocket_space = City.objects.get(name='San Francisco')
    data = {'current': None, 'destination': None}
    if request.method == 'POST':
        form = FindCity(request.POST)
        if form.is_valid():
            city = form.cleaned_data['destination']
            data = {'form': form, 'current': rocket_space, 'destination': city}
    else:
        form = FindCity()
        data = {'current': rocket_space, 'destination': None, 'form': form}
    return render(request, 'map.html', data)


def city_view(request, city_id):
    current = City.objects.get(id=city_id)
    hidden = hiding_person()
    if current == hidden:
        request.user.balance.found = True
    data = {'city': current}
    return render(request, 'city_view.html', data)