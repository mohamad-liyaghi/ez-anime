from django.shortcuts import get_object_or_404
from django.db.models import Q
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, GenericAPIView
from rest_framework.response import Response

from .serializers import TopFilmSerializer, MovieDetailSerializer, SeriesDetailSerializer, ItemListSerializer
from movie.models import Film


class AvailableApiViews(APIView):
    '''
        All available api routes. 
    '''
    allowed_methods = ('GET',)
    def get(self, request):
        api_list = [
            {"Available api list" : "/api/v1/"},
            {"10 Top rated movies" : "/api/v1/top/"},
            {"all Movies" : "/api/v1/movies/"},
            {"all series" : "/api/v1/series/"},
            {"Movie detail" : "/api/v1/movie-detail/<film id or name>/"},
            {"series detail" : "/api/v1/series-detail/<film id or name>/"},
        ]
        return Response(api_list, status=status.HTTP_200_OK)


class TopRatedMovies(ListAPIView):
    '''
        10 Top rated Movies and series
    '''
    allowed_methods = ('GET',)
    serializer_class = TopFilmSerializer
    def get_queryset(self):
        object = Film.objects.all().order_by("-ratings__average")[:10]
        return object


class SeriesApiPage(ListAPIView):
    '''
        a list of all available series in database
    '''
    allowed_methods = ('GET',)
    serializer_class = ItemListSerializer
    queryset = Film.objects.filter(~Q(seosons=0))


class MovieApiPage(ListAPIView):
    '''
        a list of all available movies in database
    '''
    allowed_methods = ('GET',)
    serializer_class = ItemListSerializer
    queryset = Film.objects.filter(Q(seosons=0))


@api_view(['GET'])
def MovieDetail(request, id):

    '''
        This route shows some extra info about selected movie, such as story, actors...
    '''

    object = get_object_or_404(Film,Q(name=id)| Q(token= id))
    if object.seosons == 0:
        serializer = MovieDetailSerializer(object)
        return Response(serializer.data)
    else:
        return Response("The item you have selected is not a movie, please return to api/v1/series-detail/<id or name>/")



@api_view(['GET'])
def SeriesDetail(request, id):

    '''
        This route shows some extra info about selected series such as  seasons, intro...
    '''

    object = get_object_or_404(Film,Q(name=id)| Q(token= id))
    if object.seosons != 0:
        serializer = SeriesDetailSerializer(object)
        return Response(serializer.data)
    else:
        return Response("The item you've selected is a movie, please return to /api/v1/movie-detail/<id or token>/")
