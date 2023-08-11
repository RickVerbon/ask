from django.contrib import admin
from base.models import Category, Comment, Question, Upvote
# Register your models here.
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Question)
admin.site.register(Upvote)
