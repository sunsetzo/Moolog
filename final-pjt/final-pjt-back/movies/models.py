from django.db import models
from django.conf import settings

# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=50)


# NowPlayingMovie 20개, UpcomingMovie 20개, PopularMoive 198개
class NowPlayingMovie(models.Model):
    # API에서 받아올 fields
    title = models.CharField(max_length=100)
    release_date = models.DateField()
    popularity = models.FloatField()
    vote_avg = models.FloatField()
    vote_count = models.IntegerField()
    overview = models.TextField()
    poster_path = models.CharField(max_length=500)
    backdrop_path = models.CharField(max_length=500, blank=True, null=True)
    genres = models.ManyToManyField(Genre)

    # 기능 구현용 fields
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_now_playing_movies')


class NowPlayingReview(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    movie = models.ForeignKey(NowPlayingMovie, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    rate = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class UpcomingMovie(models.Model):
    # API에서 받아올 fields
    title = models.CharField(max_length=100)
    release_date = models.DateField()
    popularity = models.FloatField()
    vote_avg = models.FloatField()
    vote_count = models.IntegerField()
    overview = models.TextField()
    poster_path = models.CharField(max_length=500)
    backdrop_path = models.CharField(max_length=500, blank=True, null=True)
    genres = models.ManyToManyField(Genre)

    # 기능 구현용 fields
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_upcoming_movies')


class UpcomingReview(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    movie = models.ForeignKey(UpcomingMovie, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    rate = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class PopularMovie(models.Model):
    # API에서 받아올 fields
    title = models.CharField(max_length=100)
    release_date = models.DateField()
    popularity = models.FloatField()
    vote_avg = models.FloatField()
    vote_count = models.IntegerField()
    overview = models.TextField()
    poster_path = models.CharField(max_length=500)
    backdrop_path = models.CharField(max_length=500, blank=True, null=True)
    genres = models.ManyToManyField(Genre)

    # 기능 구현용 fields
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_popular_movies')


class PopularReview(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    movie = models.ForeignKey(PopularMovie, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    rate = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)