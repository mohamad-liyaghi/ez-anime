from django.urls import path
from movie.views import AddMovie

app_name = "movie"

urlpatterns = [
    path("add-movie/",AddMovie.as_view(),name="add-movie")
]