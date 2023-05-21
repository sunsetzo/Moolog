"""my_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include

# Media, imagefield 사용
from django.conf import settings
from django.conf.urls.static import static
from dj_rest_auth.views import PasswordResetConfirmView
from dj_rest_auth.registration.views import VerifyEmailView
# from allauth.socialaccount.views import GoogleLoginView

# from accounts.views import ConfirmEmailView



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('movies.urls')),
    path('accounts/', include('dj_rest_auth.urls')),
    # 회원가입 및 회원 가입시 이메일 인증 & 비밀번호 초기화 시 이메일 전송 링크
    path('accounts/signup/', include('dj_rest_auth.registration.urls')),
    path("password-reset/confirm/<uidb64>/<token>/",
       PasswordResetConfirmView.as_view(),
       name='password_reset_confirm'),
    path('accounts/allauth/', include('allauth.urls')),
    # path('accounts/google/login/', GoogleLoginView.as_view(), name='google_login'),
    
    # 유효한 이메일을 유저에게 전달
    # re_path(r'^account-confirm-email/$', VerifyEmailView.as_view(), name='account_email_verification_sent'),
    # 유저가 클릭한 이메일(=링크) 확인
    # re_path(r'^account-confirm-email/(?P<key>[-:\w]+)/$', ConfirmEmailView.as_view(), name='account_confirm_email'),

    path('accounts/', include('accounts.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
