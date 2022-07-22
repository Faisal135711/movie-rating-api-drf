from rest_framework import serializers

from watchlist_app.models import WatchList, Drama, StreamPlatform

class WatchListSerializer(serializers.ModelSerializer):
    class Meta:
        model = WatchList
        fields = "__all__"
        # exclude = ['name']

    
class StreamPlatformSerializer(serializers.ModelSerializer):
    class Meta:
        model = StreamPlatform
        fields = "__all__"
        
        
class DramaSerializer(serializers.ModelSerializer):
    short_description = serializers.SerializerMethodField()

    class Meta:
        model = Drama 
        # exclude = ['description']
        fields = ['name', 'description', 'short_description']

    def get_short_description(self, object):
        return object.description[:2]