from rest_framework import serializers
from element.models import Genre


class GenreListSerializer(serializers.ModelSerializer):
    '''A serializer for list of genre'''

    class Meta:
        model = Genre
        fields = ["title"]


class CreateGenreSerializer(GenreListSerializer):
    '''A serializer for creating genre'''
    pass


class GenreDetailSerializer(serializers.ModelSerializer):
    '''show films with the same genre'''
    lookup_field = 'title'

    movie_genre = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Genre
        fields = ["movie_genre"]
