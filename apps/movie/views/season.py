from django.shortcuts import redirect, get_object_or_404
from django.views.generic import FormView, DetailView, UpdateView, DeleteView
from django.db import transaction
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

import uuid

from movie.models import Film, Season
from movie.forms import SeasonForm



class AddSeason(LoginRequiredMixin, FormView):
    '''
        Add seasons for series they've created
    '''

    template_name = "movie/season/add-season.html"
    form_class = SeasonForm

    # @transaction.atomic
    def form_valid(self, form):
        data = form.save(commit=False)

        # get the related series
        series = get_object_or_404(Film, token= self.kwargs['token'])

        # check if this season was not created
        if Season.objects.filter(number=data.number).exists():
            return redirect("movie:film-detail", token=series.token)

        data.token = uuid.uuid4().hex.upper()[0:10]
        data.film = series
        data.save()

        return redirect("movie:film-detail", token=series.token)


    def form_invalid(self, form):
        return redirect("movie:home")


class SeasonDetail(DetailView):
    '''
        Season detail shows extra info about a series season
    '''
    template_name = "movie/season/season-detail.html"
    def get_object(self, *args, **kwargs):
        object = get_object_or_404(Season,token=self.kwargs['token'])
        return object


class DeleteSeason(LoginRequiredMixin, DeleteView):
    '''Delete a Season'''

    template_name = "movie/movie/delete-season.html"

    def get_object(self):
        return get_object_or_404(Season, token=self.kwargs["token"])

    def get_success_url(self):
        return reverse_lazy("movie:film-detail", kwargs={"token": self.get_object().film.token})