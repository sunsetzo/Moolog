from django.contrib.auth import get_user_model
from django.contrib.auth import logout as auth_logout

from django.http import HttpResponse

from django.shortcuts import render, redirect

from rest_framework import views
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes, api_view
from rest_framework import status


from .serializers import UserSerializer

User = get_user_model()

def social_login(request):
    # data = {
    #     'detail' : '소셜회원가입이 완료되었습니다.'
    # }
    return HttpResponse("소셜회원가입이 완료되었습니다.")


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def signout(request):
    request.user.delete()
    auth_logout(request)
    data = {
        'detail' : '회원탈퇴가 완료되었습니다.'
    }
    return Response(data,status=status.HTTP_204_NO_CONTENT)



@api_view(['POST'])
@permission_classes([IsAuthenticated])
def follow(request, user_pk):
    User = get_user_model()
    person = User.objects.get(pk=user_pk)
    if person != request.user:
        if person.followers.filter(pk=request.user.pk).exists():
            person.followers.remove(request.user)
            follow = 0
        else:
            person.followers.add(request.user)
            follow = 1
        data = {
            'follow': follow
        }
        return Response(data, status=status.HTTP_202_ACCEPTED)
    
    data = {
        'detail' : '프로필 계정의 유저와 팔로우 기능을 요청한 유저는 같을 수 없습니다.'
    }
    return Response(data, status=status.HTTP_400_BAD_REQUEST)

# 프로필 이미지 저장
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def upload_image(request):
    if request.FILES.get('image'):
        image = request.FILES['image']
        user = User.objects.get(request.user)
        user.user_image = image
        user.save()
        data = {
            'detail': '사용자의 프로필 이미지가 등록되었습니다.'
        }
        return Response(data, status=status.HTTP_202_ACCEPTED)
    
    data = {
            'detail': '등록한 이미지 파일이 존재하지 않습니다.'
        }
    return Response(data, status=status.HTTP_404_NOT_FOUND)