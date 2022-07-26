from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics, mixins, viewsets
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.throttling import (
    UserRateThrottle, 
    AnonRateThrottle, 
    ScopedRateThrottle,
)
from rest_framework.filters import SearchFilter, OrderingFilter

from django.shortcuts import get_object_or_404

from django_filters.rest_framework import DjangoFilterBackend

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
from watchlist_app.api.throttling import (
    ReviewCreateThrottle,
    ReviewListThrottle,
)
from watchlist_app.api.pagination import (
    WatchListPagination,
    WatchListLOPagination,
    WatchListCPagination,
)


class UserReview(generics.ListAPIView):
    serializer_class = ReviewSerializer
    # permission_classes = [IsAuthenticated]
    # throttle_classes = [ReviewListThrottle, AnonRateThrottle]

    # def get_queryset(self):
    #     username = self.kwargs['username']
    #     return Review.objects.filter(review_user__username=username)

    def get_queryset(self):
        username = self.request.query_params.get('username', None)
        return Review.objects.filter(review_user__username=username)


class ReviewCreate(generics.CreateAPIView):
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]
    throttle_classes = [ReviewCreateThrottle]

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
    throttle_classes = [ReviewListThrottle, AnonRateThrottle]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['review_user__username', 'active']

    def get_queryset(self):
        pk = self.kwargs['pk']
        return Review.objects.filter(watchlist=pk)    


class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [ReviewUserOrReadOnly]
    # throttle_classes = [UserRateThrottle, AnonRateThrottle]
    throttle_classes = [ScopedRateThrottle]
    throttle_scope = 'review-detail'



class WatchListGV(generics.ListAPIView):
    queryset = WatchList.objects.all()
    serializer_class = WatchListSerializer      
    # filter_backends = [DjangoFilterBackend]
    # filterset_fields = ['title', 'platform__name']
    # filter_backends = [SearchFilter]
    # search_fields = ['title', 'platform__name']
    # filter_backends = [OrderingFilter]
    # ordering_filters = ['avg_rating']
    pagination_class = WatchListCPagination
    

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
    
    
