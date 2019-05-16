from django import forms
from .models import Post, Comment
from django.contrib.auth.models import User

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'img', 'contents', 'price', 'score',]

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ( 'content' ,)

class LogInForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password')
        widgets = {
            'password': forms.PasswordInput()
        }

class SignUpForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username','first_name', 'last_name', 'password', 'email')
        widgets = {
            'password': forms.PasswordInput()
        }