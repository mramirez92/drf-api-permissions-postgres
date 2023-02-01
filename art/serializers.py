from rest_framework import serializers
from .models import Art


class ArtSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id', 'owner', 'artist', 'artwork_name', 'description')
        model = Art
