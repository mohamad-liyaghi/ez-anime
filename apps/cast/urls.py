from django.urls import path
from .views import AddGenre, AddCast, CastProfile

app_name = "cast"

urlpatterns = [
    path("add-genre/",AddGenre.as_view(),name="add-genre"),
    path("add-cast/",AddCast.as_view(),name="add-cast"),
    path("profile/<str:token>/",CastProfile.as_view(),name="profile")
]