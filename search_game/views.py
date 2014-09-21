from django.shortcuts import render, redirect
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