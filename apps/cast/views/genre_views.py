from django.shortcuts import redirect
from django.views.generic import FormView
from django.contrib.auth.mixins import LoginRequiredMixin

from cast.forms import GenreForm


# Create your views here.

class AddGenre(LoginRequiredMixin, FormView):
    template_name = "cast/add-genre.html"
    form_class = GenreForm

    def form_valid(self, form):
        form.save()
        return redirect("movie:home")

    def form_invalid(self, form):
        return redirect("cast:add-genre")

