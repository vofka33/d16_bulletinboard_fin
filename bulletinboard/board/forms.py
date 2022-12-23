from ckeditor.widgets import CKEditorWidget
from django.forms import ModelForm, BooleanField
from django import forms
from .models import *
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.contrib.auth.forms import UserCreationForm
from allauth.account.forms import SignupForm
from django.contrib.auth.models import Group


# class PostForm(ModelForm):
#     check_box = BooleanField(label='Поставьте галочку для подтверждения')
#
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.fields['author'].empty_label = "Выберите автора"
#
#
#     class Meta:
#         model = Post
#         fields = ['title' , 'postCategory', 'author', 'text', 'categoryType',
#                   'check_box']
#         widgets = {
#             'text': forms.Textarea(attrs={'cols': 120, 'rows': 10}),
#         }


class PostForm(forms.ModelForm):
    text = forms.CharField(widget=CKEditorUploadingWidget())


    class Meta:
        model = Post
        fields = [ 'title', 'text', 'category']



class CommentForm(ModelForm):


    class Meta:
        model = Comment
        fields = ['text']
        widgets = {
            'text': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Текст комментария'}),
        }





