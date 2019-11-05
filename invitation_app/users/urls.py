from django.contrib import admin
from django.urls import path, include, re_path
from django.contrib.auth.decorators import login_required

from .views import register, UserProfileView

from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView, PasswordResetConfirmView, PasswordResetDoneView, PasswordResetCompleteView

urlpatterns = [
    # Authentication urls
    path('a/register/', register, name='register'),
    path('a/login/', LoginView.as_view(template_name='auth/login.html'), name='login'),
    path('a/logout/', LogoutView.as_view(template_name='auth/logout.html'), name='logout'),

    path('a/password-reset/', PasswordResetView.as_view(template_name='auth/password/reset.html'), name='password_reset'),
    path('a/password-reset/done/', PasswordResetDoneView.as_view(template_name='auth/password/done.html'), name='password_reset_done'),
    path('a/password-reset/confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name='auth/password/confirm.html'), name='password_reset_confirm'),
    path('a/password-reset/complete/', PasswordResetCompleteView.as_view(template_name='auth/password/complete.html'), name='password_reset_complete'),


    path('u/<slug:username>/', login_required(UserProfileView.as_view()), name='profile'),
]