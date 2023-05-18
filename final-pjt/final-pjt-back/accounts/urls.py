from django.urls import path
from dj_rest_auth.views import PasswordResetView

from . import views

app_name='accounts'
urlpatterns = [
    path('signout/', views.signout, name='signout'),
]