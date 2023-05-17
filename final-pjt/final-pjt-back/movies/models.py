from django.db import models
from django.conf import settings

# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=50)

class PopularMovie(models.Model):
    # API에서 받아올 fields
    title = models.CharField(max_length=100)
    release_date = models.DateField()
    popularity = models.FloatField()
    vote_avg = models.FloatField()
    vote_count = models.IntegerField()
    overview = models.TextField()
    poster_path = models.CharField(max_length=500)
    backdrop_path = models.CharField(max_length=500)
    genres = models.ManyToManyField(Genre)

    # 기능 구현용 fields
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_articles')


class UpcomingMovie(models.Model):
    # API에서 받아올 fields
    title = models.CharField(max_length=100)
    release_date = models.DateField()
    popularity = models.FloatField()
    vote_avg = models.FloatField()
    vote_count = models.IntegerField()
    overview = models.TextField()
    poster_path = models.CharField(max_length=500)
    backdrop_path = models.CharField(max_length=500)
    genres = models.ManyToManyField(Genre)

    # 기능 구현용 fields
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_articles')


class NowPlayingMovie(models.Model):
    # API에서 받아올 fields
    title = models.CharField(max_length=100)
    release_date = models.DateField()
    popularity = models.FloatField()
    vote_avg = models.FloatField()
    vote_count = models.IntegerField()
    overview = models.TextField()
    poster_path = models.CharField(max_length=500)
    backdrop_path = models.CharField(max_length=500)
    genres = models.ManyToManyField(Genre)

    # 기능 구현용 fields
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_articles')


class Review(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # class 여러개로 구분하면 세 종류의 영화리스트 중에 어떤 클래스를 참조할 지 골라야함.
    # 어차피 upcoming 20개 nowplaying 20개 개수를 정해서 받아올 거니깐 그럼 한 db에 넣고 pk로 잘라서 보내줘야할 것 같은디..?
    movie = models.ForeignKey(PopularMovie, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)