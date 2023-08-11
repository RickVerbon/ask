from django.urls import path, include
from users.views import UserCreateView, UserLoginView, UserLogoutView


urlpatterns = [
    path('register/', UserCreateView.as_view(), name="user-create-view"),
    path('login/', UserLoginView.as_view(), name="user-login-view"),
    path('logout/', UserLogoutView.as_view(), name='user-logout-view')
]
