from django import forms
from django.contrib.auth.models import User


class UserRegisterForm(forms.ModelForm):
    password = forms.CharField(max_length=50, widget=forms.PasswordInput())
    password2 = forms.CharField(max_length=50, label="Confirm password", widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'password', 'password2', 'email')
