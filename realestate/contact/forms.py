from django import forms
from .models import PostModel, CommentModel

class PostCreateForm(forms.ModelForm):
    class Meta:
        model = PostModel
        fields = ('subject','body')

class CommentCreateForm(forms.ModelForm):
    class Meta:
        model = CommentModel
        fields = ('body',)

class CommentReplyForm(forms.ModelForm):
    class Meta:
        model = CommentModel
        fields = ('body',)