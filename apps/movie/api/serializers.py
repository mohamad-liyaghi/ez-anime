from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from movie.models import Film


class TopFilmSerializer(serializers.ModelSerializer):
    '''
        Serializer for top 10 movies
    '''
    
    genre = serializers.StringRelatedField(many=True)

    class Meta:
        model = Film
        fields = ["name","imdb","genre","release_date","token"]

class MovieDetailSerializer(serializers.ModelSerializer):
    '''
        Film detail serializer
    '''

    genre = serializers.StringRelatedField(many=True)
    director = serializers.StringRelatedField(many=True)
    actors = serializers.StringRelatedField(many=True)

    class Meta:
        model = Film
        fields = ["name","imdb","actors","director","genre","release_date","intro"]
