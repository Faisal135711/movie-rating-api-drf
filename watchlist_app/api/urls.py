from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from watchlist_app.api.views import (
    WatchListAV,
    WatchDetailAV,
    StreamPlatformListAV,
    StreamPlatformDetailAV,
    StreamPlatformVS,
    ReviewList,
    ReviewDetail,
    ReviewCreate,

)

router = DefaultRouter()
router.register('stream', StreamPlatformVS, basename='streamplatform')

urlpatterns = [
    path('list/', WatchListAV.as_view(), name='movie-list'),
    path('<int:pk>/', WatchDetailAV.as_view(), name='movie-detail'),
    
    path('', include(router.urls)),

    path('<int:pk>/review-create/', ReviewCreate.as_view(), name='review-create'),
    path('<int:pk>/review/', ReviewList.as_view(), name='review-list'),
    path('review/<int:pk>/', ReviewDetail.as_view(), name='review-detail'),

]
