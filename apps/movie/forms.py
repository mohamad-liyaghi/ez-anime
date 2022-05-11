from django import forms 
from django.forms import ModelForm
from .models import Film

class MovieForm(ModelForm):
    class Meta:
        model  = Film
        fields = ("picture","name","intro","imdb","actors","director",
                "genre",
                "release_date",
                "token")

