from rest_framework.viewsets import ModelViewSet
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status


from movie.models import Film


from .seializers.film import AddSeasonSerializer, MovieListSerializer, CreateMovieSerializer, FilmDetailSerializer, SeasonListSerializer
from .permissions import MoviePermission

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

    def get_queryset(self):
        return Film.objects.all() \
            .order_by('-ratings__average')


    @action(detail=False, methods=["GET", "POST"], url_path="seasons/(?P<token>[^/.]+)")
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

