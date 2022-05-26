from django.urls import path
from .views import AvailableApiViews

urlpatterns = [
    path("", AvailableApiViews.as_view(), name="available-api"),
]