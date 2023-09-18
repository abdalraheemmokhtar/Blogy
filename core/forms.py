from django import forms
from .models import Post  # Import your Post model or the relevant model

class PostForm(forms.ModelForm):
    class Meta:
        model = Post  # Replace 'Post' with your actual model name
        fields = ['title', 'body', 'author']  # Specify the fields you want in the form
