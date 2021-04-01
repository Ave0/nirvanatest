from .models import MovieIMDB
from rest_framework import serializers



class MovieIMDBSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MovieIMDB
        fields = "__all__"
