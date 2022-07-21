from django.contrib import admin
from django.urls import path, include

from watchlist_app.api.views import (
    MovieListAV,
    MovieDetailAV,
    DramaListAV,
    DramaDetailAV
)

urlpatterns = [
    # path('list/', MovieListAV.as_view(), name='movie-list'),
    # path('<int:pk>/', MovieDetailAV.as_view(), name='movie-detail'),


    # practice
    path('', DramaListAV.as_view(), name='drama-list'),
    path('<int:pk>/', DramaDetailAV.as_view(), name='drama-detail'),
]
