from django.shortcuts import redirect, get_object_or_404
from django.views.generic import FormView, DetailView, UpdateView
from django.db import transaction
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
import uuid

from element.models import Cast, Genre
from movie.models import Film
from movie.forms import MovieForm


class AddMovie(LoginRequiredMixin, FormView):
    '''Create a new film'''

    template_name = "movie/movie/add-movie.html"
    form_class = MovieForm

    @transaction.atomic
    def form_valid(self, form):
        form = self.form_class(self.request.POST, self.request.FILES)

        form = form.save(commit=False)

        # check if film does not exist
        if Film.objects.filter(name= form.name,
                               release_date=form.release_date).exists():
            return redirect("movie:home")

        # assign a new token
        form.token = uuid.uuid4().hex.upper()[0:15]

        form.save()
        return redirect("movie:film-detail", token=form.token)

    def form_invalid(self, form):
        return redirect("movie:home")


class FilmDetail(DetailView):
    '''
        Film detail shows extra info about the object such as seasons, actors ...
    '''
    template_name = "movie/movie/movie-detail.html"
    def get_object(self, *args, **kwargs):
        object = get_object_or_404(Film,token=self.kwargs['token'])
        ip_address = self.request.user.ip_address
        if ip_address not in object.views.all():
            object.views.add(ip_address)
        return object


class UpdateMovie(LoginRequiredMixin,UpdateView):
    '''Update A Movie'''
    template_name = "movie/movie/update-movie.html"
    fields = fields = "picture", "name", "intro", "imdb", "release_date"

    def get_object(self):
        return get_object_or_404(Film, token=self.kwargs['token'])

    def get_success_url(self):
        return reverse_lazy("movie:film-detail", kwargs={ "token": self.get_object().token })

    def form_invalid(self,form):
        return redirect("movie:film-detail", self.get_object().token)

