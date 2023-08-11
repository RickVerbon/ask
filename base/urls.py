from django.urls import path
from base.views import QuestionListView, QuestionDetailView

urlpatterns = [
    path("", QuestionListView.as_view(), name="question-list-view"),
    path("question/<int:pk>", QuestionDetailView.as_view(), name="question-detail-view"),
]
