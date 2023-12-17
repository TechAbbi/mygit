from .models import MovieData
from rest_framework import serializers


class MovieDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieData
        fields = "__all__"
