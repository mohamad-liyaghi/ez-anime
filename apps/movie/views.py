from django.shortcuts import redirect, render, get_object_or_404
from django.views.generic import FormView, DetailView, UpdateView, ListView
from django.db import transaction
from django.contrib.auth.mixins import LoginRequiredMixin
import uuid

from cast.models import Cast, Genre
from movie.models import Film, season
from .forms import MovieForm, CastForm, SeriesForm, AddSeason

# Create your views here.

def HomePage(request):
    '''
        Home page includes List of recent movies, genres and top rated item
    '''
    films = Film.objects.all().order_by('-ratings__average')
    genre = Genre.objects.all()
    return render(request,"base/home.html",{"films" : films,"genres" : genre})

class FilmDetail(DetailView):
    '''
        Film detail shows extra info about the object such as seasons, actors ...
    '''
    template_name = "base/movie-detail.html"
    def get_object(self, *args, **kwargs):
        object = get_object_or_404(Film,token=self.kwargs['token'])
        ip_address = self.request.user.ip_address
        print(object.views.all())
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


class AddMovie(LoginRequiredMixin, FormView):
    '''
        This class let admins to add items
    '''
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
        

class AddSeries(LoginRequiredMixin, FormView):
    '''
        This page let admins to add series
    '''
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


class UpdateSeries(LoginRequiredMixin,UpdateView):
    '''
        This page let admins to update series
    '''
    template_name = "movie/update-series.html"
    fields = "picture","name","intro","imdb","seosons","release_date","token"
    success_url = "/"
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
        actor.works.add(film)

class AddFilmCast(FormView):
    '''
        Admins can add extra Actors/directors to the series they have created
    '''
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
        return redirect('movie:add-season', token=self.kwargs['token'])
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
        form.token= token=uuid.uuid4().hex.upper()[0:10]
        form.save()
        film_model = Film.objects.filter(token=self.kwargs['token'])
        for film in film_model:
            form.for_film.add(film)
            film.seoson_story.add(form)
        return redirect('movie:home')
    def form_invalid(self, form):
        print(form.errors)


def search_film(request):
    #Search film func
	if request.method == "POST":
		searched = request.POST['search_field']
		film = Film.objects.filter(name__contains=searched)	
		return render(request, 
		'base/search-result.html', 
		{'searched':searched,
		'film':film})
	else:
		return render(request, 
		'base/search-result.html', 
		{})

class SearchFilm(ListView):
    '''
        Result of items that user searched for
    '''
    template_name = 'base/search-result.html'
    def get_queryset(self):
        return Film.objects.filter(name__icontains=self.kwargs['name'])

class FilterGenre(ListView):
    '''
        Filter movies by genre
    '''
    template_name = 'movie/filter-film.html'
    def get_queryset(self):
        print(self.kwargs['genre'])
        return Film.objects.filter(genre__title__in= [self.kwargs['genre']])


def handler404(request, exception=None):
    '''
        404 page
    '''
    return render(request, "base/errors/404.html", {})

def handler500(request, exception=None):
    '''
        500 error page
    '''
    return render(request, "base/errors/500.html", {})