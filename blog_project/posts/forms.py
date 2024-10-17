from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        mode=Post
        fields='__all__'