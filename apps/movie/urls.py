from django.urls import path
from movie.views import HomePage, AddMovie, AddCast, AddSeries, AddSeason, FilmDetail, SeasonDetail

app_name = "movie"

urlpatterns = [
    path("",HomePage,name="home"),
    path("detail/<str:token>/",FilmDetail.as_view(),name="film-detail"),
    path("season-detail/<str:token>/",SeasonDetail.as_view(),name="season-detail"),
    path("add-movie/",AddMovie.as_view(),name="add-movie"),
    path("add-series/",AddSeries.as_view(),name="add-series"),
    path("add-cast/<str:token>/",AddCast.as_view(),name="add-cast"),
    path("add-season/<str:token>/",AddSeason.as_view(),name="add-season"),
]