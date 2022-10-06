from django.urls import path
from .views.cast import AddCast, UpdateCast, CastProfile, AddActorToMovie, AddDirectorToMovie, remove_actor_from_movie
from .views.genre import  AddGenre, AddGenreToMovie, remove_genre_from_movie

app_name = "element"

urlpatterns = [
    path("add-genre/",AddGenre.as_view(),name="add-genre"),
    path("add-cast/",AddCast.as_view(),name="add-cast"),
    path('add-actor/<str:token>/', AddActorToMovie.as_view(), name="add-actor-to-movie"),
    path('add-director/<str:token>/', AddDirectorToMovie.as_view(), name="add-director-to-movie"),
    path('remove-actor/<str:film>/<str:actor>/', remove_actor_from_movie, name="remove-actor-from-movie"),
    path('remove-genre/<str:film>/<str:genre>/', remove_genre_from_movie, name="remove-genre-from-movie"),


    path('add-genre/<str:token>/', AddGenreToMovie.as_view(), name="add-genre-to-movie"),


    path("update-cast/<str:token>/",UpdateCast.as_view(),name="update-cast"),
    path("cast-profile/<str:token>/",CastProfile.as_view(),name="profile")
]