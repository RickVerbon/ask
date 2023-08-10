from django.urls import path, include
from users.views import UserCreateView, UserLoginView

urlpatterns = [
    path('register/', UserCreateView.as_view(), name="user-create-view"),
    path('login/', UserLoginView.as_view(), name="user-login-view"),
]
