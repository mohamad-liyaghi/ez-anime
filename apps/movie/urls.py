from django.urls import path
from .views.film import (
    AddMovie, UpdateMovie,
       FilmDetail, DeleteMovie)

from .views.core import (
        HomePage, SearchFilm, FilterGenre
)

from .views.season import AddSeason, SeasonDetail

app_name = "movie"

urlpatterns = [
    path("", HomePage, name="home"),

    path("movie-detail/<str:token>/", FilmDetail.as_view(), name="film-detail"),
    path("season-detail/<str:token>/", SeasonDetail.as_view(), name="season-detail"),
    path("add-movie/", AddMovie.as_view(), name="add-movie"),
    path("update-movie/<str:token>/", UpdateMovie.as_view(), name="update-movie"),
    path("delete-movie/<str:token>/", DeleteMovie.as_view(), name="delete-movie"),
    path("add-season/<str:token>/", AddSeason.as_view(), name="add-season"),
    path("search/<str:name>/", SearchFilm.as_view(), name="search-film"),
    path("filter-genre/<str:genre>/", FilterGenre.as_view(), name="filter-genre"),
]

