from django.contrib.auth.models import User
from django.forms import ModelForm
from django import forms

class UserForm(ModelForm):
    class Meta:
        model=User
        fields=('username','email','password')

