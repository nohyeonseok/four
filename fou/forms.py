from django import forms
from .models import Portfolio, Comment

class NewBlog(forms.ModelForm):

    class Meta:
        model = Portfolio
        fields = ('title', 'description','image')

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields=('author', 'message')