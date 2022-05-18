from django.urls import path
from movie.views import (HomePage, 
    AddMovie, UpdateMovie,
     AddFilmCast,UpdateSeries,
      AddSeries, AddSeason,
       FilmDetail, SeasonDetail,SearchFilm)

app_name = "movie"

urlpatterns = [
    path("",HomePage,name="home"),
    path("detail/<str:token>/",FilmDetail.as_view(),name="film-detail"),
    path("season-detail/<str:token>/",SeasonDetail.as_view(),name="season-detail"),
    path("add-movie/",AddMovie.as_view(),name="add-movie"),
    path("update-movie/<str:token>/",UpdateMovie.as_view(),name="update-movie"),
    path("add-series/",AddSeries.as_view(),name="add-series"),
    path("update-series/<str:token>/",UpdateSeries.as_view(),name="update-series"),
    path("add-cast/<str:token>/",AddFilmCast.as_view(),name="add-cast"),
    path("add-season/<str:token>/",AddSeason.as_view(),name="add-season"),
    path("search/<str:name>/",SearchFilm.as_view(),name="search-film"),
]
