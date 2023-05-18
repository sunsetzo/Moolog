from rest_framework import generics
from rest_framework.permissions import AllowAny
from django.contrib.auth import get_user_model
from .serializers import CustomUserSerializer, CustomLoginSerializer

from django.shortcuts import render, redirect

from rest_framework import views
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
from rest_framework import status

from django.views.decorators.http import require_POST, require_safe, require_http_methods
# from .forms import CustomUserCreationForm, CustomUserChangeForm
User = get_user_model()

class CustomUserCreate(generics.CreateAPIView):
    permission_classes = [AllowAny]
    queryset = User.objects.all()
    serializer_class = CustomUserSerializer




class LoginView(views.APIView):
    def post(self, request):
        serializer = CustomLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        # 로그인 후 수행할 작업

        return Response({"message": "로그인 성공"})





# 회원 탈퇴 및 정보수정
# @require_http_methods(['POST'])
# def delete(request):
#     request.user.delete()
#     auth_logout(request)
#     return redirect('articles:index')

# def update(request):
#     if request.method == 'POST':
#         form = CustomUserChangeForm(request.POST, instance=request.user)
#         if form.is_valid():
#             form.save()
#             return redirect('articles:index') 
#     else:
#         form = CustomUserChangeForm(instance=request.user)
#     context = {'form': form}
#     return render(request, 'accounts/update.html', context)


# def profile(request, username):
#     User = get_user_model()
#     person = User.objects.get(username=username)
#     context = {
#         'person': person,
#     }
#     return render(request, 'accounts/profile.html', context)


# 팔로우/ 되는지 확인해야 함!
@require_POST
@permission_classes([IsAuthenticated])
def follow(request, user_pk):
    User = get_user_model()
    person = User.objects.get(pk=user_pk)
    if person != request.user:
        if person.followers.filter(pk=request.user.pk).exists():
            person.followers.remove(request.user)
        else:
            person.followers.add(request.user)
    serializer = CustomUserSerializer(User)
    return Response(serializer.data, status=status.HTTP_200_OK)