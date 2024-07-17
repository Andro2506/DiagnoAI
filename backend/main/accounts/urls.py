from django.urls import path
from accounts.views import UserRegistrationView, UserLoginView, UserProfileView, UserChangePasswordView, SendPasswordResetEmailView, UserPasswordResetView, AccessCheckView

urlpatterns = [
    path('register/', UserRegistrationView, name='register'),
    path('login/', UserLoginView, name='login'),
    path('profile/', UserProfileView, name='profile'),
    path('changepassword/', UserChangePasswordView, name='changepassword'),
    path('send-reset-password-email/', SendPasswordResetEmailView, name='send-reset-password-email'),
    path('reset-password/<uid>/<token>/', UserPasswordResetView, name='profile'),
    path('access-check/', AccessCheckView, name='access-check'),
]