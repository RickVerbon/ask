from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from base.models import Question

# Create your views here.


class QuestionListView(ListView):
    model = Question
    template_name = "base/question_list_view.html"
    context_object_name = "questions"


class QuestionDetailView(DetailView):
    model = Question


class QuestionCreateView(LoginRequiredMixin, CreateView):
    model = Question
    fields = ('title', 'text', 'category')

    def form_valid(self, form):
        print(self.request.user)
        print(self.request.user.profile)
        form.instance.author = self.request.user.profile
        return super().form_valid(form)
