from django.contrib import admin
from django.urls import path, include

from watchlist_app.api.views import (
    MovieListAV,
    MovieDetailAV,
)

urlpatterns = [
    path('list/', MovieListAV.as_view(), name='movie-list'),
    path('<int:pk>/', MovieDetailAV.as_view(), name='movie-detail'),


    # practice
    # path('', drama_list, name='drama-list'),
    # path('<int:pk>/', drama_details, name='drama-detail'),
]
