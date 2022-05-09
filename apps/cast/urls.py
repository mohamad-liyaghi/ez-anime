from django.urls import path
from .views import AddGenre,AddCast

app_name = "cast"

urlpatterns = [
    path("add-genre/",AddGenre.as_view(),name="add-genre"),
    path("add-cast/",AddCast.as_view(),name="add-cast")
]