from rest_framework import serializers

from watchlist_app.models import Movie, Drama

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = "__all__"
        # exclude = ['name']
        
        
class DramaSerializer(serializers.Serializer):
    pass