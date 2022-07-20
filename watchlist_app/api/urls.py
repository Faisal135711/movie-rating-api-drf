from django.contrib import admin
from django.urls import path, include

from watchlist_app.api.views import (
    movie_list,
    movie_details,
    drama_list,
    drama_details
)

urlpatterns = [
    path('list/', movie_list, name='movie-list'),
    # path('<int:pk>/', movie_details, name='movie-detail'),


    # practice
    path('', drama_list, name='drama-list'),
    path('<int:pk>/', drama_details, name='drama-detail'),
]
