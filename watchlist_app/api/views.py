from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics, mixins, viewsets
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle

from django.shortcuts import get_object_or_404

from watchlist_app.api.permission import AdminOrReadOnly, ReviewUserOrReadOnly

from watchlist_app.models import (
    WatchList, 
    StreamPlatform, 
    Review,

)
from watchlist_app.api.serializers import (
    WatchListSerializer, 
    StreamPlatformSerializer,
    ReviewSerializer,

)


class ReviewCreate(generics.CreateAPIView):
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Review.objects.all()

    def perform_create(self, serializer):
        pk = self.kwargs['pk']
        watchlist = WatchList.objects.get(pk=pk)

        review_user = self.request.user
        review_queryset = Review.objects.filter(watchlist=watchlist, review_user=review_user)

        if review_queryset.exists():
            raise ValidationError("You have already reviewed this movie.")

        if watchlist.number_rating == 0:
            watchlist.avg_rating = serializer.validated_data['rating']
        else:
            watchlist.avg_rating = (watchlist.avg_rating + serializer.validated_data['rating']) / 2
        
        watchlist.number_rating += 1
        watchlist.save()

        serializer.save(watchlist=watchlist, review_user=review_user)


class ReviewList(generics.ListAPIView):
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]
    throttle_classes = [UserRateThrottle, AnonRateThrottle]

    def get_queryset(self):
        pk = self.kwargs['pk']
        return Review.objects.filter(watchlist=pk)    


class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [ReviewUserOrReadOnly]
    throttle_classes = [UserRateThrottle, AnonRateThrottle]
    

class WatchListAV(APIView):
    permission_classes = [AdminOrReadOnly]
    
    def get(self, request):
        movies = WatchList.objects.all()  
        serializer = WatchListSerializer(movies, many=True)      
        return Response(serializer.data)
    
    def post(self, request):
        serializer = WatchListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class WatchDetailAV(APIView):
    permission_classes = [AdminOrReadOnly]

    def get(self, request, pk):
        try:
            movie = WatchList.objects.get(pk=pk)
        except:
            return Response({'error': 'Not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = WatchListSerializer(movie)
        return Response(serializer.data)
    
    def put(self, request, pk):
        try:
            movie = WatchList.objects.get(pk=pk)
        except:
            return Response({'error': 'Not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = WatchListSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        try:
            movie = WatchList.objects.get(pk=pk)
        except:
            return Response({'error': 'Not found'}, status=status.HTTP_404_NOT_FOUND)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

class StreamPlatformVS(viewsets.ModelViewSet):
    queryset = StreamPlatform.objects.all()
    serializer_class = StreamPlatformSerializer
    permission_classes = [AdminOrReadOnly]


# class StreamPlatformVS(viewsets.ViewSet):
#     def list(self, request):
#         queryset = StreamPlatform.objects.all()
#         serializer = StreamPlatformSerializer(queryset, many=True)
#         return Response(serializer.data)

#     def retrieve(self, request, pk=None):
#         queryset = StreamPlatform.objects.all()
#         watchlist = get_object_or_404(queryset, pk=pk)
#         serializer = StreamPlatformSerializer(watchlist)
#         return Response(serializer.data)

#     def create(self, request):
#         serializer = StreamPlatformSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)

    
class StreamPlatformListAV(APIView):
    permission_classes = [AdminOrReadOnly]

    def get(self, request):
        streams = StreamPlatform.objects.all()
        serializer = StreamPlatformSerializer(streams, many=True, context={'request': request})
        return Response(serializer.data)

    def post(self, request):
        serializer = StreamPlatformSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
        
class StreamPlatformDetailAV(APIView):
    permission_classes = [AdminOrReadOnly]

    def get(self, request, pk):
        try:
            stream = StreamPlatform.objects.get(pk=pk)
        except:
            return Response({'error': 'Not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = StreamPlatformSerializer(stream, context={'request': request})
        return Response(serializer.data)
    
    def put(self, request, pk):
        try:
            stream = StreamPlatform.objects.get(pk=pk)
        except:
            return Response({'error': 'Not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = StreamPlatformSerializer(stream, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
    def delete(self, request, pk):
        try:
            stream = StreamPlatform.objects.get(pk=pk)
        except:
            return Response({'error': 'Not found'}, status=status.HTTP_404_NOT_FOUND)
        stream.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    
