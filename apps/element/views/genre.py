from django.shortcuts import redirect
from django.views.generic import FormView
from django.contrib.auth.mixins import LoginRequiredMixin

from element.forms import GenreForm
from element.models import Genre


class AddGenre(LoginRequiredMixin, FormView):
    '''Add a genre to db'''

    template_name = "element/genre/add-genre.html"
    form_class = GenreForm

    def form_valid(self, form):
        title = form.cleaned_data.get("title")

        if Genre.objects.filter(title=title).exists():
            return redirect("movie:home")

        form.save()
        return redirect("movie:home")

    def form_invalid(self, form):
        return redirect("element:add-genre")

