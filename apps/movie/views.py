from django.shortcuts import redirect
from django.views.generic import FormView
from django.db import transaction

import uuid

from cast.models import Cast,Genre
from movie.models import Film
from .forms import MovieForm, CastForm, SeriesForm

# Create your views here.
class AddMovie(FormView):
    template_name = "movie/add-movie.html"
    form_class = MovieForm
    @transaction.atomic
    def form_valid(self, form):
        form = self.form_class(self.request.POST, self.request.FILES)
        form = form.save(commit=False)
        form.token = uuid.uuid4().hex.upper()[0:15]
        form.save()
        return redirect("movie:add-cast", token=form.token)

    def form_invalid(self,form):
        print(form.errors)

class AddSeries(FormView):
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
            global genre
            for genre in genres:
                film.genre.add(genre)
                genre.films_related.add(film)
            for director in director_cast:
                film.director.add(director)
                director.works.add(film)
                director.genre.add(genre)
            for actor_1 in Cast.objects.filter(full_name=actor1_field):
                film.actors.add(actor_1)
                actor_1.works.add(film)
                actor_1.genre.add(genre)
            for actor_2 in Cast.objects.filter(full_name=actor2_field):
                film.actors.add(actor_2)
                actor_2.works.add(film)
                actor_2.genre.add(genre)
            for actor_3 in Cast.objects.filter(full_name=actor3_field):
                film.actors.add(actor_3)
                actor_3.works.add(film)
                actor_3.genre.add(genre)
            for actor_4 in Cast.objects.filter(full_name=actor4_field):
                film.actors.add(actor_4)
                actor_4.works.add(film)
                actor_4.genre.add(genre)
      
    def form_invalid(self,form):
        print(form.errors)


