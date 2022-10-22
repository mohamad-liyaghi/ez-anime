from rest_framework import serializers
from movie.models import Film, Season


class MovieListSerializer(serializers.ModelSerializer):
    '''List of all movies '''

    class Meta:
        model = Film
        fields = ["picture", "name", "imdb", 'release_date', 'token']



class CreateMovieSerializer(serializers.ModelSerializer):
    '''Add A movie to db'''

    token = serializers.CharField(read_only=True)

    class Meta:
        model = Film
        fields = ["picture", "name", "intro", "imdb", 'release_date', 'token']


class SeasonListSerializer(serializers.Serializer):
    '''Show Season name and token for a film'''

    number = serializers.IntegerField(read_only=True)
    token = serializers.CharField(read_only=True)
    # the dude that is related to detail page




class FilmDetailSerializer(serializers.ModelSerializer):
    '''Detail page of a movie'''
    
    lookup_field = "token"
    extra_kwargs = {
        'url': {'lookup_field': 'token'}
    }

    actors = serializers.StringRelatedField(read_only=True, many=True)
    director = serializers.StringRelatedField(read_only=True, many=True)
    genre = serializers.StringRelatedField(read_only=True, many=True) 
    token = serializers.CharField(read_only=True)   
    
    # add season here after creating season detail

    class Meta:
        model = Film
        fields = ["picture", "name", "intro", "imdb", "release_date", "token",
            "actors", "director", "genre", "seasons"
        ]

class AddSeasonSerializer(serializers.ModelSerializer):
    '''Add a season for a film'''

    token = serializers.CharField(read_only=True)

    class Meta:
        model = Season
        fields = ["number", "story", "token"]


class SeasonDetailSerializer(serializers.ModelSerializer):
    '''Detail Page of a season'''
    
    film = serializers.StringRelatedField()

    class Meta:
        model = Season
        fields = ["number", "story", "token", "film"]