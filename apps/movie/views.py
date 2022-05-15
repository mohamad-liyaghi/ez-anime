from django.shortcuts import redirect, render
from django.views.generic import FormView, ListView
from django.db import transaction
from django.contrib.auth.mixins import LoginRequiredMixin
import uuid

from cast.models import Cast, Genre
from movie.models import Film
from .forms import MovieForm, CastForm, SeriesForm, AddSeason

# Create your views here.

def HomePage(request):
    films = Film.objects.all()
    genre = Genre.objects.all()
    return render(request,"base/home.html",{"films" : films,"genres" : genre})
    

class AddMovie(LoginRequiredMixin, FormView):
    template_name = "movie/add-movie.html"
    form_class = MovieForm

    @transaction.atomic
    def form_valid(self, form):
        form = self.form_class(self.request.POST, self.request.FILES)
        form = form.save(commit=False)
        form.token = uuid.uuid4().hex.upper()[0:15]
        form.save()
        return redirect("movie:add-cast", token=form.token)

    def form_invalid(self, form):
        print(form.errors)


class AddSeries(LoginRequiredMixin, FormView):
    template_name = "movie/add-series.html"
    form_class = SeriesForm

    @transaction.atomic
    def form_valid(self, form):
        form = self.form_class(self.request.POST, self.request.FILES)
        form = form.save(commit=False)
        form.token = uuid.uuid4().hex.upper()[0:15]
        form.save()
        return redirect("movie:add-cast", token=form.token)

    def form_invalid(self, form):
        print(form.errors)


def AddActor(full_name, film):
    for actor in Cast.objects.filter(full_name=full_name):
        film.actors.add(actor)
        actor.works.add(film)

class AddCast(FormView):
    template_name = "movie/add-cast.html"
    form_class = CastForm
    @transaction.atomic
    def form_valid(self, form,**kwargs):
        director_field = self.request.POST["director_field"]
        actor1_field = self.request.POST["actor1_field"]
        actor2_field = self.request.POST["actor2_field"]
        actor3_field = self.request.POST["actor3_field"]
        actor4_field = self.request.POST["actor4_field"]
        genre_field = self.request.POST["genre"]
        film_model = Film.objects.filter(token=self.kwargs['token'])
        genres = Genre.objects.filter(title=genre_field)
        director_cast = Cast.objects.filter(full_name=director_field)
        for film in film_model:
            global movie_genre
            for movie_genre in genres:
                film.genre.add(movie_genre)
                movie_genre.films_related.add(film)
            AddActor(actor1_field,film)
            AddActor(actor2_field,film)
            AddActor(actor3_field,film)
            AddActor(actor4_field,film)
            for director in director_cast:
                film.director.add(director)
                director.works.add(film)
            
    def form_invalid(self,form):
        print(form.errors)

class AddSeason(LoginRequiredMixin, FormView):
    template_name = "movie/add-season.html"
    form_class = AddSeason
    @transaction.atomic
    def form_valid(self, form):
        form = form.save()
        film_model = Film.objects.filter(token=self.kwargs['token'])
        for film in film_model:
            form.for_film.add(film)
            film.seoson_story.add(form)

    def form_invalid(self, form):
        print(form.errors)