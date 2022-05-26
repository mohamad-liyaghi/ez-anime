from django.urls import path
from .views import (AvailableApiViews, TopRatedMovies)

urlpatterns = [
    path("", AvailableApiViews.as_view(), name="available-api"),
    path("top/", TopRatedMovies.as_view(), name="top-movie-api"),
]