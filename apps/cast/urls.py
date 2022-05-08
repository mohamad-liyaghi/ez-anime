from django.urls import path
from .views import AddGenre

name = "cast"

urlpatterns = [
    path("add-genre/",AddGenre.as_view(),name="add-genre"),
]