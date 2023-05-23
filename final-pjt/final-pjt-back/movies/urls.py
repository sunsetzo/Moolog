from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    # 현재 상영작
    path('now_playing_movies/', views.now_playing_movie_list),
    path('now_playing_movies/<int:movie_id>/', views.now_playing_movie_detail),
    path('now_playing_movies/reviews/', views.now_playing_movie_review_list),
    path('now_playing_movies/reviews/<int:review_pk>/', views.now_playing_movie_review_detail),
    path('now_playing_movies/<int:movie_id>/reviews/', views.now_playing_movie_review_create),
    path('now_playing_movies/<int:movie_id>/likes/', views.now_playing_movies_likes, name='now_playing_movies_likes'),

    # 개봉 예정작
    path('upcoming_movies/', views.upcoming_movie_list),
    path('upcoming_movies/<int:movie_id>/', views.upcoming_movie_detail),
    path('upcoming_movies/reviews/', views.upcoming_movie_review_list),
    path('upcoming_movies/reviews/<int:review_pk>/', views.upcoming_movie_review_detail),
    path('upcoming_movies/<int:movie_id>/reviews/', views.upcoming_movie_review_create),
    path('upcoming_movies/<int:movie_id>/likes/', views.upcoming_movies_likes),

    # 인기작
    path('popular_movies/', views.popular_movie_list),
    path('popular_movies/scroll/<int:page_pk>/', views.popular_movie_scroll),
    path('popular_movies/<int:movie_id>/', views.popular_movie_detail),
    path('popular_movies/reviews/', views.popular_movie_review_list),
    path('popular_movies/reviews/<int:review_pk>/', views.popular_movie_review_detail),
    path('popular_movies/<int:movie_id>/reviews/', views.popular_movie_review_create),
    path('popular_movies/<int:movie_id>/likes/', views.popular_movies_likes),

    # 추천 영화
    path('recommend_movies/', views.recommend_movie_list),
]
