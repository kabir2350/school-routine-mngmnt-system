from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.db import models  
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    email = forms.EmailField(label = "Email")
    # fullname = forms.CharField(label = "Full name")

    class Meta:
        model = User
        fields = ("username", "email", )

