from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from search_game.models import City


class CreateSearch(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'password2',
        ]


class FindCity(forms.Form):
    destination = forms.ModelChoiceField(queryset=City.objects.all())
