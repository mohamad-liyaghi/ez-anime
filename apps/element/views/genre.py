from django.shortcuts import redirect, get_object_or_404
from django.views.generic import FormView
from django.contrib.auth.mixins import LoginRequiredMixin

from element.forms import GenreForm, MovieGenreForm
from movie.models import Film
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



class AddGenreToMovie(LoginRequiredMixin, FormView):
    '''Add Genre for a movie'''

    form_class = MovieGenreForm
    template_name = "element/genre/add-genre-to-film.html"

    def form_valid(self, form):

        film = get_object_or_404(Film,
                                 token=self.kwargs["token"])

        genre = get_object_or_404(Genre, title=form.cleaned_data["genre"])

        if not genre in film.genre.all():
            film.genre.add(genre)
            return redirect("movie:movie-detail", token=film.token)

        return redirect("movie:movie-detail", token=film.token)


    def form_invalid(self, form):
        return redirect("movie:home")