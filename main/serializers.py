from rest_framework import serializers

from main.models import Artist, Album, Song


class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ['name', 'email', 'phone', 'id']


class AlbumSerializer(serializers.ModelSerializer):
    artists = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Album
        fields = ['name', 'release_year', 'id', 'artists']


class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ['title', 'duration', 'album', 'id']


class ArtistAlbumSerializer(serializers.ModelSerializer):
    # albums = serializers.StringRelatedField(read_only=True, many=True)
    albums = AlbumSerializer(many=True, read_only=True)

    class Meta:
        model = Artist
        fields = ["name", "phone", "albums"]
