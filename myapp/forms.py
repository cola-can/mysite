from django import forms
from .models import Post
from dataclasses import fields

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content',)