from django.urls import path, include
from users.views import UserCreateView

urlpatterns = [
    path('register/', UserCreateView.as_view(), name="user-create-view")
]
