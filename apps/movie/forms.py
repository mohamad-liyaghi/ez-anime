from django import forms 
from django.forms import ModelForm
from movie.models import Film, Season

class MovieForm(ModelForm):
    '''A form for creating Movies'''

    class Meta:
        model  = Film
        fields = ["name", "picture", "intro", "imdb", "release_date"]


class SeasonForm(ModelForm):
    '''A form for adding season to series'''

    class Meta:
        model = Season
        fields = ["number", "film", "story"]
