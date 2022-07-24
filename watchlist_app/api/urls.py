from django.contrib import admin
from django.urls import path, include

from watchlist_app.api.views import (
    WatchListAV,
    WatchDetailAV,
    StreamPlatformListAV,
    StreamPlatformDetailAV,
    DramaListAV,
    DramaDetailAV,
    DramaStreamPlatformListAV,
    DramaStreamPlatformDetailAV,
)

urlpatterns = [
    # path('list/', WatchListAV.as_view(), name='movie-list'),
    # path('<int:pk>/', WatchDetailAV.as_view(), name='movie-detail'),
    
    # path('stream/', StreamPlatformListAV.as_view(), name='stream-list'),
    # path('stream/<int:pk>/', StreamPlatformDetailAV.as_view(), name='stream-detail'),

    # practice
    path('list/', DramaListAV.as_view(), name='drama-list'),
    path('<int:pk>/', DramaDetailAV.as_view(), name='drama-detail'),

    path('stream/', DramaStreamPlatformListAV.as_view(), name='stream-list'),
    path('stream/<int:pk>/', DramaStreamPlatformDetailAV.as_view(), name='stream-detail'),
]
