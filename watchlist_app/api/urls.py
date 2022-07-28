from django.contrib import admin
from django.urls import path, include

from watchlist_app.api.views import (
    WatchListAV,
    WatchDetailAV,
    StreamPlatformListAV,
    StreamPlatformDetailAV,
    ReviewList,
    ReviewDetail,

    DramaListAV,
    DramaDetailAV,
    DramaStreamPlatformListAV,
    DramaStreamPlatformDetailAV,
)

urlpatterns = [
    path('list/', WatchListAV.as_view(), name='movie-list'),
    path('<int:pk>/', WatchDetailAV.as_view(), name='movie-detail'),
    
    path('stream/', StreamPlatformListAV.as_view(), name='streamplatform-list'),
    path('stream/<int:pk>/', StreamPlatformDetailAV.as_view(), name='streamplatform-detail'),

    path('review/', ReviewList.as_view(), name='review-list'),
    path('review/<int:pk>/', ReviewDetail.as_view(), name='review-detail'),

    # practice
    # path('list/', DramaListAV.as_view(), name='drama-list'),
    # path('<int:pk>/', DramaDetailAV.as_view(), name='drama-detail'),

    # path('stream/', DramaStreamPlatformListAV.as_view(), name='stream-list'),
    # path('stream/<int:pk>/', DramaStreamPlatformDetailAV.as_view(), name='stream-detail'),
]
