from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView

from watchlist_app.models import Movie, Drama
from watchlist_app.api.serializers import MovieSerializer, DramaSerializer


class MovieListAV(APIView):
    def get(self, request):
        movies = Movie.objects.all()  
        serializer = MovieSerializer(movies, many=True)      
        return Response(serializer.data)
    
    def post(self, request):
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class MovieDetailAV(APIView):
    def get(self, request, pk):
        try:
            movie = Movie.objects.get(pk=pk)
        except:
            return Response({'error': 'Movie not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = MovieSerializer(movie)
        return Response(serializer.data)
    
    def put(self, request, pk):
        try:
            movie = Movie.objects.get(pk=pk)
        except:
            return Response({'error': 'Movie not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = MovieSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        try:
            movie = Movie.objects.get(pk=pk)
        except:
            return Response({'error': 'Movie not found'}, status=status.HTTP_404_NOT_FOUND)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    
class DramaListAV(APIView):
    def get(self, request):
        dramas = Drama.objects.all()
        serializer = DramaSerializer(dramas, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = DramaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
        
class DramaDetailAV(APIView):
    def get(self, request, pk):
        try:
            drama = Drama.objects.get(pk=pk)
        except:
            return Response({'error': 'Drama not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = DramaSerializer(drama)
        return Response(serializer.data)
    
    def put(self, request, pk):
        try:
            drama = Drama.objects.get(pk=pk)
        except:
            return Response({'error': 'Drama not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = DramaSerializer(drama, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
    def delete(self, request, pk):
        try:
            drama = Drama.objects.get(pk=pk)
        except:
            return Response({'error': 'Drama not found'}, status=status.HTTP_404_NOT_FOUND)
        drama.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        