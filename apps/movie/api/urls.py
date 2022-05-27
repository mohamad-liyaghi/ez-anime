from django.urls import path
from .views import (AvailableApiViews, TopRatedMovies, MovieApiPage, SeriesApiPage, MovieDetail, SeriesDetail)

urlpatterns = [
    path("", AvailableApiViews.as_view(), name="available-api"),
    path("top/", TopRatedMovies.as_view(), name="top-movie-api"),
    path("series/", SeriesApiPage.as_view(),name="series-api"),
    path("movies/", MovieApiPage.as_view(),name="movie-api"),
    path("movie-detail/<str:id>/", MovieDetail, name="film-detail-api"),
    path("series-detail/<str:id>/", SeriesDetail, name="series-detail-api"),
]