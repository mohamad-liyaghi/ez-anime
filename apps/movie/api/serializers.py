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