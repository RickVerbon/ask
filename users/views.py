from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.models import User
from users.forms import UserRegisterForm
# Create your views here.


class UserCreateView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'users/user_register.html'
    success_url = reverse_lazy('user-login')

    def form_valid(self, form):
        password = form.cleaned_data.get('password')
        password2 = form.cleaned_data.get('password2')
        print(password, password2)
        if str(password) != str(password2):
            return HttpResponse("Password's do not match, user not created")

        user = form.save(commit=False)
        user.set_password(password)
        user.save()

        return super().form_valid(form)
