from django.urls import path
from base.views import QuestionListView, QuestionDetailView, QuestionCreateView

urlpatterns = [
    path("", QuestionListView.as_view(), name="question-list-view"),
    path("question/<int:pk>", QuestionDetailView.as_view(), name="question-detail-view"),
    path("question/create", QuestionCreateView.as_view(), name="question-create-view")
]
