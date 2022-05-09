from django import  forms
from django.forms import ModelForm
from .models import Genre,Cast

class GenreForm(ModelForm):
    class Meta:
        model = Genre
        fields = ('title','films_related')

class CastForm(ModelForm):
    class Meta:
        model = Cast
        fields = ("avatar","full_name","biography","birthday","genre","works","role")

