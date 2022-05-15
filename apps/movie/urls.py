from django.urls import path
from movie.views import HomePage, AddMovie, AddCast, AddSeries, AddSeason

app_name = "movie"

urlpatterns = [
    path("",HomePage,name="home"),
    path("add-movie/",AddMovie.as_view(),name="add-movie"),
    path("add-series/",AddSeries.as_view(),name="add-series"),
    path("add-cast/<str:token>/",AddCast.as_view(),name="add-cast"),
    path("add-season/<str:token>/",AddSeason.as_view(),name="add-season"),
]