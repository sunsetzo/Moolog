from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    path('now_playing_movies/', views.now_playing_movie_list),
    path('now_playing_movies/<int:movie_id>/', views.now_playing_movie_detail),
    path('now_playing_movies/reviews/', views.now_playing_movie_review_list),
    path('now_playing_movies/reviews/<int:review_pk>/', views.now_playing_movie_review_detail),
    path('now_playing_movies/<int:movie_id>/reviews/', views.now_playing_movie_review_create),
]
