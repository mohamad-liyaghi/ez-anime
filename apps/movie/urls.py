from django.urls import path
from movie.views import AddMovie, AddCast, AddSeries

app_name = "movie"

urlpatterns = [
    path("add-movie/",AddMovie.as_view(),name="add-movie"),
    path("add-series/",AddSeries.as_view(),name="add-series"),
    path("add-cast/<str:token>/",AddCast.as_view(),name="add-cast")
]