from django.urls import path
from base.views import (QuestionListView,
                        QuestionDetailView,
                        QuestionCreateView,
                        QuestionUpdateView,
                        QuestionDeleteView,
                        CommentCreateView,
                        UpvoteView,)

urlpatterns = [
    path("", QuestionListView.as_view(), name="question-list-view"),
    path("question/create", QuestionCreateView.as_view(), name="question-create-view"),
    path("question/<int:pk>", QuestionDetailView.as_view(), name="question-detail-view"),
    path("question/<int:pk>/edit", QuestionUpdateView.as_view(), name="question-update-view"),
    path("question/<int:pk>/delete", QuestionDeleteView.as_view(), name="question-delete-view"),
    path('question/<int:question_id>/upvote/', UpvoteView.as_view(), name='upvote-view'),
    path('question/<int:pk>/comment', CommentCreateView.as_view(), name="comment-create-view"),
]
