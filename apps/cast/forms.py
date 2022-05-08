from django import  forms
from django.forms import ModelForm
from .models import Genre

class CastForm(ModelForm):
    class Meta:
        model = Genre
        fields = ('title','films_related')