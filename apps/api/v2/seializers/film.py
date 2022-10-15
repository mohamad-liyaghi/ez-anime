from rest_framework import serializers
from movie.models import Film


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