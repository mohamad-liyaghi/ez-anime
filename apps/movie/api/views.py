from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.response import Response

from .serializers import TopFilmSerializer 
from movie.models import Film


class AvailableApiViews(APIView):
    '''
        All available api routes. 
    '''
    allowed_methods = ('GET',)
    def get(self, request):
        return Response({"Available api list" : "/api/v1/"}, status=status.HTTP_200_OK)

class TopRatedMovies(ListAPIView):
    '''
        10 Top rated Movies and series
    '''
    serializer_class = TopFilmSerializer
    def get_queryset(self):
        object = Film.objects.all().order_by("-ratings__average")[:10]
        return object