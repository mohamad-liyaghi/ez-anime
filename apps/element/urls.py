from django.urls import path
from .views.cast import AddCast, UpdateCast, CastProfile
from .views.genre import  AddGenre

app_name = "element"

urlpatterns = [
    path("add-genre/",AddGenre.as_view(),name="add-genre"),
    path("add-cast/",AddCast.as_view(),name="add-cast"),
    path("update-cast/<str:token>/",UpdateCast.as_view(),name="update-cast"),
    path("cast-profile/<str:token>/",CastProfile.as_view(),name="profile")
]