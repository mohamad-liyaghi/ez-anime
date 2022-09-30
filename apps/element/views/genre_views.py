from django.shortcuts import redirect
from django.views.generic import FormView
from django.contrib.auth.mixins import LoginRequiredMixin

from element.forms import GenreForm


# Create your views here.

class AddGenre(LoginRequiredMixin, FormView):
    template_name = "element/add-genre.html"
    form_class = GenreForm

    def form_valid(self, form):
        form.save()
        return redirect("movie:home")

    def form_invalid(self, form):
        return redirect("element:add-genre")

