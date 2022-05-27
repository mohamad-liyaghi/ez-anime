from django.urls import include
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


class ItemListSerializer(TopFilmSerializer):
    '''
        Item list serializer
    '''
    
    genre = serializers.StringRelatedField(many=True)

    class Meta:
        model = Film
        fields = TopFilmSerializer.Meta.fields + ["seosons"]



class MovieDetailSerializer(TopFilmSerializer):
    '''
        Film detail serializer
    '''

    genre = serializers.StringRelatedField(many=True)
    director = serializers.StringRelatedField(many=True)
    actors = serializers.StringRelatedField(many=True)

    class Meta:
        model = Film
        fields = TopFilmSerializer.Meta.fields +  ["actors","director","intro"]


class SeriesDetailSerializer(MovieDetailSerializer):
    '''
        Series detail serializer
    '''
    
    seoson_story = serializers.StringRelatedField(read_only=True, many=True)
    class Meta:
        model = Film
        fields = MovieDetailSerializer.Meta.fields +  ["seosons", "seoson_story"]
        
