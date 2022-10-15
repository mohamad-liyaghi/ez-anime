from django.urls import path, include
from rest_framework_nested import routers
from . import views

app_name = 'v2'


router = routers.DefaultRouter()

router.register('film', views.FilmViewSet, basename="film")


urlpatterns = [
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
]

urlpatterns += router.urls
