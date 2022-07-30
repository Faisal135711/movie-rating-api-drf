from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics, mixins

from watchlist_app.models import (
    WatchList, 
    StreamPlatform, 
    Review,

    Drama,
    DramaStreamPlatform,
    DramaReview
)
from watchlist_app.api.serializers import (
    WatchListSerializer, 
    StreamPlatformSerializer,
    ReviewSerializer,

    DramaSerializer,
    DramaStreamPlatformSerializer,
    DramaReviewSerializer
)


class ReviewList(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    

class WatchListAV(APIView):
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
    
    
class StreamPlatformListAV(APIView):
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
    
    
#practice

class DramaReviewListAV(mixins.ListModelMixin,
                        generics.GenericAPIView):
    queryset = DramaReview.objects.all()
    serializer_class = DramaReviewSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class DramaReviewDetailAV(mixins.RetrieveModelMixin,
                        mixins.CreateModelMixin,
                        generics.GenericAPIView):
    queryset = DramaReview.objects.all()
    serializer_class = DramaReviewSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


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
        

class DramaStreamPlatformListAV(APIView):
    def get(self, request):
        platforms = DramaStreamPlatform.objects.all()
        serializer = DramaStreamPlatformSerializer(platforms, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = DramaStreamPlatformSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class DramaStreamPlatformDetailAV(APIView):
    def get(self, request, pk):
        try:
            platform = DramaStreamPlatform.objects.get(pk=pk)
        except:
            return Response({'error': 'Not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = DramaStreamPlatformSerializer(platform)
        return Response(serializer.data)

    def put(self, request, pk):
        try:
            platform = DramaStreamPlatform.objects.get(pk=pk)
        except:
            return Response({'error': 'Not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = DramaStreamPlatformSerializer(platform, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


    def delete(self, request, pk):
        try:
            platform = DramaStreamPlatform.objects.get(pk=pk)
        except:
            return Response({'error': 'Not found'}, status=status.HTTP_404_NOT_FOUND)
        platform.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
 
