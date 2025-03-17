from django import forms
from .models import Post, Comment
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from taggit.forms import TagWidget 

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']





class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']
        widgets = {
            'tags': TagWidget(),  # Use TagWidget for tag input
        }
    def save(self, commit=True):
        instance = super().save(commit=False)
        tags_list = self.cleaned_data['tags'].split(',')
        instance.save()
        instance.tags.set(tags_list)  # Assign tags to the post
        return instance

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Write a comment...'}),
        }
