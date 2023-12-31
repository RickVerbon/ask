from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    avatar = models.ImageField(default='avatars/default.jpg', upload_to="avatars/")
    bio = models.TextField(max_length=300, blank=True)
    language = models.CharField(max_length=30, blank=True)

    def __str__(self):
        return self.user.username
