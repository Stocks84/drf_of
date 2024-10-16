from rest_framework import serializers
from .models import Game, Comment, Like

class GameSerializer(serializers.ModelSerializer):
    creator = serializers.ReadOnlyField(source='creator.username')

    class Meta:
        model = Game
        fields = ('id', 'title', 'description', 'creator', 'created_at', 'updated_at')

class CommentSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Comment
        fields = ('id', 'user', 'game', 'content', 'created_at')

class LikeSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Like
        fields = ('id', 'user', 'game')