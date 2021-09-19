"""Users URLs."""

# Django
from django.urls import path

# Views
from cride.users.views import (
    UserLoginAPIView,
    UserSignUpAPIView,
    AccountVerificationAPIView,
)

urlpatterns = [
    path('users/login', UserLoginAPIView.as_view(), name='login'),
    path('users/singup/', UserSignUpAPIView.as_view(), name='singup'),
    path('users/verify/', AccountVerificationAPIView.as_view(), name='verify'),
]