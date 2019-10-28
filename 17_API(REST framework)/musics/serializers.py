from rest_framework import serializers
from .models import Music, Artist, Comment

class MusicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Music
        fields = ('id', 'title', 'artist',)

class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ('id', 'name',)

class ArtistDetailSerializer(serializers.ModelSerializer):
    music = MusicSerializer(source='music_set', many=True)
    musics_count = serializers.IntegerField(source='music_set.count')
    class Meta:
        model = Artist
        fields = ('id', 'name', 'music', 'musics_count',)

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'music_id', 'content',)