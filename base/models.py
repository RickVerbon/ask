from django.db import models
from users.models import Profile


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)


class Question(models.Model):
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    question_title = models.CharField(max_length=200)
    question_text = models.TextField(max_length=2000)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    upvotes = models.IntegerField()


class Comment(models.Model):
    author = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="comments_written")
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="comments")
    text = models.TextField(max_length=2000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Upvote(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="upvote")
    post = models.ForeignKey(Question, on_delete=models.CASCADE)  # Or Comment, depending on your use case

    class Meta:
        unique_together = ['user', 'post']  # Enforces one upvote per user per post
