from django.urls import path
from .views.cast_views import AddCast, UpdateCast, CastProfile
from .views.genre_views import  AddGenre

app_name = "element"

urlpatterns = [
    path("add-genre/",AddGenre.as_view(),name="add-genre"),
    path("add-element/",AddCast.as_view(),name="add-element"),
    path("update-element/<str:token>/",UpdateCast.as_view(),name="update-element"),
    path("profile/<str:token>/",CastProfile.as_view(),name="profile")
]