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

def get_city_choices():
    return City.objects.all()

class FindCity(forms.Form):
    name = forms.ChoiceField(choices=get_city_choices())
    test = forms.CharField(max_length=40)


