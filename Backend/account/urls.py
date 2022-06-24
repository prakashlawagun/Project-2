from django.urls import path
from account.views import *

urlpatterns = [
    path('register/',UserRegistrationView.as_view(),name="register"),
    path('login/',UserLoginView.as_view(),name="login"),
    path('profile/',UserProfileView.as_view(),name="profile"),
    path('change-password/',UserChangePasswordView.as_view(),name="change-password"),
]
