from django.shortcuts import redirect, get_object_or_404
from django.views.generic import FormView, DetailView, UpdateView
from django.db import transaction
from django.contrib.auth.mixins import LoginRequiredMixin
import uuid

from element.models import Cast, Genre
from movie.models import Film, season
from movie.forms import MovieForm, CastForm, AddSeason


class AddMovie(LoginRequiredMixin, FormView):
    '''Create a new film'''

    template_name = "movie/add-movie.html"
    form_class = MovieForm

    @transaction.atomic
    def form_valid(self, form):
        form = self.form_class(self.request.POST, self.request.FILES)

        form = form.save(commit=False)

        # check if film does not exist
        if Film.objects.filter(name= form.name,
                               release_date=form.release_date).exists():
            print("wtf dude")
            return redirect("movie:home")

        # assign a new token
        form.token = uuid.uuid4().hex.upper()[0:15]

        form.save()
        return redirect("movie:movie-detail", token=form.token)

    def form_invalid(self, form):
        return redirect("movie:home")


class FilmDetail(DetailView):
    '''
        Film detail shows extra info about the object such as seasons, actors ...
    '''
    template_name = "base/movie-detail.html"
    def get_object(self, *args, **kwargs):
        object = get_object_or_404(Film,token=self.kwargs['token'])
        ip_address = self.request.user.ip_address
        if ip_address not in object.views.all():
            object.views.add(ip_address)
        return object


class SeasonDetail(DetailView):
    '''
        Season detail shows extra info about a series season
    '''
    template_name = "movie/season-detail.html"
    def get_object(self, *args, **kwargs):
        object = get_object_or_404(season,token=self.kwargs['token'])
        return object


class UpdateMovie(LoginRequiredMixin,UpdateView):
    '''
        This item let admins to update movies
    '''
    template_name = "movie/update-movie.html"
    fields = fields = "picture","name","intro","imdb","release_date","token"
    success_url ="/"
    
    def get_object(self):
        return get_object_or_404(Film, token=self.kwargs['token'])

    def form_invalid(self,form):
        print(form.errors)


def AddActor(full_name, film):
    '''
        This func is for AddFilmCast class, admins can add director and actors to the movies
    '''
    for actor in Cast.objects.filter(full_name=full_name):
        film.actors.add(actor)

class AddFilmCast(FormView):
    '''
        Admins can add extra Actors/directors to the series they have created
    '''
    template_name = "movie/add-element.html"
    form_class = CastForm
    @transaction.atomic
    def form_valid(self, form,**kwargs):
        film_model = Film.objects.filter(token=self.kwargs['token']).first()
        genres = Genre.objects.filter(title= self.request.POST["genre"]).first()
        director = Cast.objects.filter(full_name= self.request.POST["director_field"]).first()

        film_model.genre.add(genres)
        film_model.director.add(director)

        AddActor(self.request.POST["actor1_field"], film_model)
        AddActor(self.request.POST["actor2_field"], film_model)
        AddActor(self.request.POST["actor3_field"], film_model)
        AddActor(self.request.POST["actor4_field"], film_model)

        return redirect('movie:film-detail', token=self.kwargs['token'])

    def form_invalid(self,form):
        print(form.errors)


class AddSeason(LoginRequiredMixin, FormView):
    '''
        Add seasons for series they've created
    '''
    template_name = "movie/add-season.html"
    form_class = AddSeason
    @transaction.atomic
    def form_valid(self, form):
        form = form.save(commit=False)
        form.token= uuid.uuid4().hex.upper()[0:10]
        form.save()
        film_model = Film.objects.filter(token=self.kwargs['token'])
        for film in film_model:
            form.for_film.add(film)
            film.seoson_story.add(form)
        return redirect('movie:home')
    def form_invalid(self, form):
        print(form.errors)

