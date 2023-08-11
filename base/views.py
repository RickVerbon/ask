from django.shortcuts import render
from django.views.generic import ListView, DetailView
from base.models import Question

# Create your views here.


class QuestionListView(ListView):
    model = Question
    template_name = "base/question_list_view.html"
    context_object_name = "questions"


class QuestionDetailView(DetailView):
    model = Question
