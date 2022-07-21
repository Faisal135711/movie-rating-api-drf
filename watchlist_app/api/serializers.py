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
        
        
class DramaSerializer(serializers.Serializer):
    pass