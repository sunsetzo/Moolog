from django.db import models
from django.conf import settings

# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=50)


# NowPlayingMovie 20개, PopularMovie 20개, PopularMoive 100개
class Movie(models.Model):
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
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_movies')



class Review(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    rate = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)