from rest_framework import serializers
from .models import NowPlayingMovie, UpcomingMovie, PopularMovie, Genre
from .models import NowPlayingReview, UpcomingReview, PopularReview


class GenreListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Genre
        fields = '__all__'


class NowPlayingMovieListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = NowPlayingMovie
        fields = '__all__'
        read_only_fields = ('genres', 'like_users',)


class NowPlayingMovieReviewSerializer(serializers.ModelSerializer):
    nickname = serializers.CharField(max_length=20, source='user.nickname', read_only=True, required=False) 
    userimage = serializers.ImageField(read_only=True, required=False)

    class Meta:
        model = NowPlayingReview
        fields = '__all__'
        read_only_fields = ('user', 'movie',)


class NowPlayingMovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = NowPlayingMovie
        fields = '__all__'