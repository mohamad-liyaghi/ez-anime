from django import forms 
from django.forms import ModelForm
from movie.models import Film, season

class MovieForm(ModelForm):
    '''A form for creating Movies'''

    class Meta:
        model  = Film
        fields = ["name", "picture", "intro", "imdb", "release_date"]

class CastForm(forms.Form):
    director_field = forms.CharField(required=False)
    actor1_field = forms.CharField(required=False)
    actor2_field = forms.CharField(required=False)
    actor3_field = forms.CharField(required=False)
    actor4_field = forms.CharField(required=False)
    genre = forms.CharField(required=False)



class AddSeason(ModelForm):
    class Meta:
        model = season
        fields = "season_number", "for_film", "story"
