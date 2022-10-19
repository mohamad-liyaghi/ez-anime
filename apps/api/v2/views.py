from rest_framework.viewsets import ModelViewSet
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status


from movie.models import Film, Season
from element.models import Cast



from .seializers.film import (AddSeasonSerializer, MovieListSerializer, CreateMovieSerializer, FilmDetailSerializer,
                                SeasonListSerializer, SeasonDetailSerializer)

from .seializers.cast import (CastListSerializer)

from .permissions import MoviePermission, CastPermission

class FilmViewSet(ModelViewSet):
    '''A Viewset for Get/Create/Update/Detail a movie'''
    
    permission_classes = [MoviePermission,]
    lookup_field = 'token'

    def get_serializer_class(self):
        # find appropriate serializer
        if self.action == "list":
            return MovieListSerializer
        
        # serializer for create movie
        elif self.action == "create":
            return CreateMovieSerializer

        elif self.action in ["update", "partial_update", "delete", "retrieve", "metadata"]:
            return FilmDetailSerializer

        elif self.action == "get_season_list" and self.request.method == "GET":
            return SeasonListSerializer

        elif self.action == "get_season_list" and self.request.method == "POST":
            return AddSeasonSerializer

        elif self.action == "season_detail" and self.request.method == 'GET':
            return SeasonDetailSerializer
        
        elif self.action == "season_detail" and self.request.method in ['PUT', 'PATCH']:
            return AddSeasonSerializer

    def get_queryset(self):
        return Film.objects.all() \
            .order_by('-ratings__average')


    @action(detail=False, methods=["GET", "POST"], url_path="(?P<token>[^/.]+)/seasons")
    # list of seasons
    def get_season_list(self, request, token):
        if request.method == "GET":

            film = get_object_or_404(Film, token=token)
            seasons = film.seasons.all()
            serializer = SeasonListSerializer(seasons, many=True)
            return Response(serializer.data)

        if request.method == "POST":
            # create a season
            film = get_object_or_404(Film, token=token)
            serializer = AddSeasonSerializer(data=request.data)    

            if serializer.is_valid():
                serializer.save(film=film)
                return Response(serializer.data, status=status.HTTP_201_CREATED)

            return Response({"error" : "invalid information"}, status=status.HTTP_403_FORBIDDEN)


    @action(detail=False, methods=["GET", "PATCH", "PUT", "DELETE"], url_path="(?P<film>[^/.]+)/seasons/(?P<season>[^/.]+)")
    # season detail
    def season_detail(self, request, film, season):
        if request.method == "GET":

            film = get_object_or_404(Film, token=film)
            season = get_object_or_404(Season, film=film, token=season)

            serializer = SeasonDetailSerializer(season)
            return Response(serializer.data)


        if request.method in ["PUT", "PATCH"]:
            # create a season
            film = get_object_or_404(Film, token=film)
            season = get_object_or_404(Season, film=film, token=season)
            serializer = AddSeasonSerializer(season, data=request.data, partial=True)

            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)



class CastViewSet(ModelViewSet):
    '''A viewset for cast (add/delete/update/retrieve etc.)'''

    permission_classes =[CastPermission,]
    queryset = Cast.objects.all()


    def get_serializer_class(self):
        
        if self.action == "list":
            return CastListSerializer