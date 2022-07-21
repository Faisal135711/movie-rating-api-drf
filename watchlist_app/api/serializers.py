from rest_framework import serializers

from watchlist_app.models import Movie, Drama

class MovieSerializer(serializers.ModelSerializer):
    name_len = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = "__all__"
        # exclude = ['name']

    def get_name_len(self, object):
        return len(object.name)
        
        
class DramaSerializer(serializers.ModelSerializer):
    short_description = serializers.SerializerMethodField()

    class Meta:
        model = Drama 
        # exclude = ['description']
        fields = ['name', 'description', 'short_description']

    def get_short_description(self, object):
        return object.description[:2]