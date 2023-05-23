from rest_framework import serializers
from .models import NowPlayingMovie, UpcomingMovie, PopularMovie, Genre
from .models import NowPlayingReview, UpcomingReview, PopularReview


class GenreListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Genre
        fields = '__all__'


# 현재 상영작
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

    def validate_rate(self, value):
        if value % 0.5 != 0:
            raise serializers.ValidationError('0.5 단위로 별점을 입력해주세요.')
        return value


class NowPlayingMovieSerializer(serializers.ModelSerializer):
    nowplayingreview_set = NowPlayingMovieReviewSerializer(many=True, read_only=True)
    genres = GenreListSerializer(many=True, read_only=True)

    class Meta:
        model = NowPlayingMovie
        fields = '__all__'
        read_only_fields = ('genres', 'like_users', 'genres',)



# 개봉 예정작
class UpcomingMovieListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = UpcomingMovie
        fields = '__all__'
        read_only_fields = ('genres', 'like_users',)


class UpcomingMovieReviewSerializer(serializers.ModelSerializer):
    nickname = serializers.CharField(max_length=20, source='user.nickname', read_only=True, required=False) 
    userimage = serializers.ImageField(read_only=True, required=False)

    class Meta:
        model = UpcomingReview
        fields = '__all__'
        read_only_fields = ('user', 'movie',)

    
    def validate_rate(self, value):
        if value % 0.5 != 0:
            raise serializers.ValidationError('0.5 단위로 별점을 입력해주세요.')
        return value


class UpcomingMovieSerializer(serializers.ModelSerializer):
    upcomingreview_set = UpcomingMovieReviewSerializer(many=True, read_only=True)
    genres = GenreListSerializer(many=True, read_only=True)

    class Meta:
        model = UpcomingMovie
        fields = '__all__'
        read_only_fields = ('genres', 'like_users', 'genres',)


# 인기 영화
class PopularMovieListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = PopularMovie
        fields = '__all__'
        read_only_fields = ('genres', 'like_users',)


class PopularMovieReviewSerializer(serializers.ModelSerializer):
    nickname = serializers.CharField(max_length=20, source='user.nickname', read_only=True, required=False) 
    userimage = serializers.ImageField(read_only=True, required=False)

    class Meta:
        model = PopularReview
        fields = '__all__'
        read_only_fields = ('user', 'movie',)

    def validate_rate(self, value):
        if value % 0.5 != 0:
            raise serializers.ValidationError('0.5 단위로 별점을 입력해주세요.')
        return value


class PopularMovieSerializer(serializers.ModelSerializer):
    popularreview_set = PopularMovieReviewSerializer(many=True, read_only=True)
    genres = GenreListSerializer(many=True, read_only=True)

    class Meta:
        model = PopularMovie
        fields = '__all__'
        read_only_fields = ('genres', 'like_users', 'genres',)