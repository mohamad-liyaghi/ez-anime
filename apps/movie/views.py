from django.views.generic import FormView

import uuid

from cast.models import Cast,Genre
from movie.models import Film
from .forms import MovieForm

# Create your views here.
class AddMovie(FormView):
    template_name = "movie/add-movie.html"
    form_class = MovieForm
    def form_valid(self, form):
        form = self.form_class(self.request.POST, self.request.FILES)
        genre_field = self.request.POST.get("genre_field")

        form = form.save(commit=False)
        form.token = uuid.uuid4().hex.upper()[0:15]
        form.save()

    def form_invalid(self,form):
        print(form.errors)
        