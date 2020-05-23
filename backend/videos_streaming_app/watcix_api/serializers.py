from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Movie


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('id', 'Uploader_name', 'Name_of_movie', 'Genre_of_movie',
                  'Duration_of_movie', 'Rating')


class MovieMiniSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('id', 'Name_of_movie', 'Genre_of_movie')
