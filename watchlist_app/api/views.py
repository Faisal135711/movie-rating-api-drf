from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from watchlist_app.models import Movie
from watchlist_app.api.serializers import MovieSerializer

@api_view(['GET', 'POST'])
def movie_list(request):
    if request.method == 'GET':
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True) 
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else: 
            return Response(serializer.errors)

@api_view(['GET', 'PUT', 'DELETE'])
def movie_details(request, pk):
    if request.method == 'GET':
        try:
            movie = Movie.objects.get(pk=pk)
        except Movie.DoesNotExist:
            return Response({'error': 'Movie not found' },  status=status.HTTP_404_NOT_FOUND)
        serializer = MovieSerializer(movie) 
        return Response(serializer.data)
    
    if request.method == 'PUT':
        try:
            movie = Movie.objects.get(pk=pk)
        except Movie.DoesNotExist:
            return Response({'error': 'Movie not found' },  status=status.HTTP_404_NOT_FOUND)
        serializer = MovieSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
    if request.method == 'DELETE':
        try:
            movie = Movie.objects.get(pk=pk)
        except Movie.DoesNotExist:
            return Response({'error': 'Movie not found' },  status=status.HTTP_404_NOT_FOUND)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)