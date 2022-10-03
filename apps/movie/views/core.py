from django.shortcuts import render
from django.views.generic import  ListView


from element.models import Cast, Genre
from movie.models import Film


# Create your views here.

def HomePage(request):
    '''
        Home page includes List of recent movies, genres and top rated item
    '''
    films = Film.objects.all().order_by('-ratings__average')
    genre = Genre.objects.all()
    return render(request, "base/home.html", {"films": films, "genres": genre})


def search_film(request):
    # Search film func
    if request.method == "POST":
        searched = request.POST['search_field']
        film = Film.objects.filter(name__contains=searched)
        return render(request,
                      'base/search-result.html',
                      {'searched': searched,
                       'film': film})
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
        return Film.objects.filter(genre__title__in=[self.kwargs['genre']])


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