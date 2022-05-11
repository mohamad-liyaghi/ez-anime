from django.urls import path
from movie.views import AddMovie, AddCast

app_name = "movie"

urlpatterns = [
    path("add-movie/",AddMovie.as_view(),name="add-movie"),
    path("add-cast/<str:token>/",AddCast.as_view(),name="add-cast")
]