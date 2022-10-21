from rest_framework import serializers
from element.models import Genre


class GenreListSerializer(serializers.ModelSerializer):
    '''A serializer for list of genre'''

    class Meta:
        model = Genre
        fields = ["title"]
