from django.shortcuts import render, redirect
from search_game.models import City
from world import settings
from search_game.forms import CreateSearch

# Create your views here.


def home(request):
    return render(request, 'home.html')


def register(request):
    if request.method == 'POST':
        form = CreateSearch(request.POST)
        if form.is_valid():
            current_user = form.save()
            current_user.email_user('Welcome!', 'Thanks for joining our website.', settings.DEFAULT_FROM_EMAIL)

            return redirect('profile')
    else:
        form = CreateSearch()
    return render(request, 'registration/register.html', {'form': form})


def profile(request):
    return render(request, 'profile.html')

def map(request):
    rocket_space = City.objects.filter(name='San Francisco')[1]
    data = {'city': rocket_space}
    return render(request, 'map.html', data)

def city_view(request, city_id):
    pass