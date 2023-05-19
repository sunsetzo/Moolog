from django.urls import path
from . import views

app_name='accounts'
urlpatterns = [
    path('signout/', views.signout, name='signout'),
    path('follow/<int:user_pk>/', views.follow, name='follow'),
    path('profile_image/', views.upload_image, name='upload_image'),
]