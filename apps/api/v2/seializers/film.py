from rest_framework import serializers
from movie.models import Film


class MovieListSerializer(serializers.ModelSerializer):
    '''List of all movies '''
    class Meta:
        model = Film
        fields = ["picture", "name", "imdb", 'release_date', 'token']