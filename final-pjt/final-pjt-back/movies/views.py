from rest_framework.response import Response
from rest_framework.decorators import api_view

from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from django.shortcuts import get_list_or_404, get_object_or_404
from .serializers import NowPlayingMovieSerializer, NowPlayingMovieListSerializer, NowPlayingMovieReviewSerializer
from .models import NowPlayingMovie, NowPlayingReview

# Create your views here.
@api_view(['GET'])
def now_playing_movie_list(request):
    movies = get_list_or_404(NowPlayingMovie)
    serializer = NowPlayingMovieListSerializer(movies, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def now_playing_movie_detail(request, movie_id):
    movie = get_object_or_404(NowPlayingMovie, pk=movie_id)
    serializer = NowPlayingMovieSerializer(movie)
    return Response(serializer.data)


@api_view(['GET'])
def now_playing_movie_review_list(request):
    reviews = get_list_or_404(NowPlayingReview)
    serializer = NowPlayingMovieReviewSerializer(reviews, many=True)
    return Response(serializer.data)


# 현재 상영작 리뷰 조회, 삭제, 수정
@api_view(['GET', 'DELETE', 'PUT'])
def now_playing_movie_review_detail(request, review_pk):
    review = get_object_or_404(NowPlayingReview, pk=review_pk)

    if request.method == 'GET':
        serializer = NowPlayingMovieReviewSerializer(review)
        return Response(serializer.data)
    
    elif request.method == 'DELETE':
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    elif request.method == 'PUT':
        serializer = NowPlayingMovieReviewSerializer(review, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        


# 현재 상영작 리뷰 생성
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def now_playing_movie_review_create(request, movie_id):
    movie = get_object_or_404(NowPlayingMovie, pk=movie_id)
    print(movie)
    serializer = NowPlayingMovieReviewSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(user=request.user, movie=movie)
        return Response(serializer.data, status=status.HTTP_201_CREATED)