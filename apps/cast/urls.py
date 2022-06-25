from django.urls import path
from .views.cast_views import AddCast, UpdateCast, CastProfile
from .views.genre_views import  AddGenre

app_name = "cast"

urlpatterns = [
    path("add-genre/",AddGenre.as_view(),name="add-genre"),
    path("add-cast/",AddCast.as_view(),name="add-cast"),
    path("update-cast/<str:token>/",UpdateCast.as_view(),name="update-cast"),
    path("profile/<str:token>/",CastProfile.as_view(),name="profile")
]