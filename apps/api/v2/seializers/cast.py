from rest_framework import serializers
from element.models import Cast


class CastListSerializer(serializers.ModelSerializer):
    '''List of all Casts'''

    class Meta:
        model = Cast
        fields = ["avatar", "full_name", "role", "token"]