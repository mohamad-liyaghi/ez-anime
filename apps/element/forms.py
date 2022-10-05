from django import  forms
from django.forms import ModelForm
from .models import Genre,Cast

class GenreForm(ModelForm):
    class Meta:
        model = Genre
        fields = ('title',)

class CastForm(ModelForm):
    class Meta:
        model = Cast
        fields = ("avatar","full_name","biography","birthday","role")


class MovieActorForm(ModelForm):
    actor = forms.ModelChoiceField(queryset= Cast.objects.filter(role="a"))
    class Meta:
        model =  Cast
        fields = ["actor"]


class MovieDirectorForm(ModelForm):
    director = forms.ModelChoiceField(queryset= Cast.objects.filter(role="d"))

    class Meta:
        model =  Cast
        fields = ["director"]


class MovieGenreForm(ModelForm):
    genre = forms.ModelChoiceField(queryset= Genre.objects.all())

    class Meta:
        model = Genre
        fields = ["genre"]