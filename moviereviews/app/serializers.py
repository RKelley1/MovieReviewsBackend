from rest_framework import serializers
from .models import Comment, Movie
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'id']

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['title']

class CommentSerializer(serializers.ModelSerializer):
    movie = MovieSerializer(many=False, read_only=True)
    user = UserSerializer(many=False, read_only=True)
    class Meta:
        model = Comment
        fields = ['id','movie','user', 'content','upvotes']
        