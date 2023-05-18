from rest_framework import generics
from rest_framework.permissions import AllowAny
from django.contrib.auth import get_user_model
from django.contrib.auth import logout as auth_logout

from django.shortcuts import render, redirect

from rest_framework import views
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes, api_view
from rest_framework import status

from django.views.decorators.http import require_POST, require_safe, require_http_methods


from .serializers import CustomUserSerializer

User = get_user_model()

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def signout(request):
    request.user.delete()
    auth_logout(request)
    context = {
        'detail' : '회원탈퇴가 완료되었습니다.'
    }
    return Response(context,status=status.HTTP_204_NO_CONTENT)



# 수정해야함.....
@api_view(['POST'])
# @permission_classes([IsAuthenticated])
def follow(request, user_pk):
    User = get_user_model()
    person = User.objects.get(pk=user_pk)
    if person != request.user:
        if person.followers.filter(pk=request.user.pk).exists():
            person.followers.remove(request.user)
        else:
            person.followers.add(request.user)
    serializer = CustomUserSerializer(person)
    return Response(serializer.data, status=status.HTTP_200_OK)