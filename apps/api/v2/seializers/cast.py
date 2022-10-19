from rest_framework import serializers
from element.models import Cast


class CastListSerializer(serializers.ModelSerializer):
    '''List of all Casts'''

    class Meta:
        model = Cast
        fields = ["avatar", "full_name", "role", "token"]


class CreateCastSerializer(serializers.ModelSerializer):
    '''A serializer for creating Casts'''

    token = serializers.CharField(read_only=True)

    class Meta:
        model = Cast
        fields = ["avatar", "full_name", "role", "biography", "birthday", "token"]


class CastDetailSerializer(CreateCastSerializer):
    '''Detail page of an actor/director'''
    lookup_field = 'token'
    pass