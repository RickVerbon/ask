from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from django.views.decorators.http import require_POST
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from base.models import Question, Upvote, Comment
from base.mixins import IsAuthorMixin


# Create your views here.


class QuestionListView(ListView):
    model = Question
    template_name = "base/question_list_view.html"
    context_object_name = "questions"
    ordering = ['-created_at']


class QuestionDetailView(DetailView):
    model = Question
    success_url = reverse_lazy('question-list-view')


class QuestionCreateView(LoginRequiredMixin, CreateView):
    model = Question
    fields = ('title', 'text', 'category')

    def form_valid(self, form):
        form.instance.author = self.request.user.profile
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('question-detail-view', kwargs={'pk': self.object.pk})


class QuestionUpdateView(LoginRequiredMixin, IsAuthorMixin, UpdateView):
    model = Question
    fields = ('title', 'text', 'category')

    def get_success_url(self):
        return reverse_lazy('question-detail-view', kwargs={'pk': self.object.pk})


class QuestionDeleteView(LoginRequiredMixin, IsAuthorMixin, DeleteView):
    model = Question
    success_url = reverse_lazy('question-list-view')


class UpvoteView(LoginRequiredMixin, View):
    def post(self, request, question_id):
        question = get_object_or_404(Question, id=question_id)

        # Check if the user has already upvoted this question
        upvote_exists = Upvote.objects.filter(user=request.user.profile, question=question).exists()

        if not upvote_exists:
            # Create a new upvote instance
            Upvote.objects.create(user=request.user.profile, question=question)
        else:
            upvote = Upvote.objects.get(user=request.user.profile, question=question)
            upvote.delete()

        # Calculate and get the updated upvote count for the question
        updated_upvote_count = question.upvote_set.count()

        return HttpResponse(updated_upvote_count)


class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    fields = ('text',)

    def form_valid(self, form):
        question_pk = self.kwargs['pk']
        form.instance.author = self.request.user.profile
        form.instance.question_id = question_pk
        return super().form_valid(form)

    def get_success_url(self):
        question_pk = self.kwargs['pk']
        return reverse_lazy('question-detail-view', kwargs={'pk': question_pk})
