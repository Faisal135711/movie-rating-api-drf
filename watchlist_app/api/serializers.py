from rest_framework import serializers

from watchlist_app.models import (
    WatchList, 
    StreamPlatform,
    Drama, 
    DramaStreamPlatform,
)

class WatchListSerializer(serializers.ModelSerializer):
    class Meta:
        model = WatchList
        fields = "__all__"
        # exclude = ['name']

    
class StreamPlatformSerializer(serializers.ModelSerializer):
    watchlist = WatchListSerializer(many=True, read_only=True)
    class Meta:
        model = StreamPlatform
        fields = "__all__"
        
        
class DramaSerializer(serializers.ModelSerializer):
    short_description = serializers.SerializerMethodField()

    class Meta:
        model = Drama
        fields = "__all__" 
        # exclude = ['description']
        # fields = ['name', 'description', 'short_description']

    def get_short_description(self, object):
        return object.description[:2]


class DramaStreamPlatformSerializer(serializers.ModelSerializer):
    class Meta:
        model = DramaStreamPlatform
        fields = "__all__"