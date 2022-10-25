from django.contrib import admin
from django import forms
from .models import Comment, Post
from ckeditor_uploader.widgets import CKEditorUploadingWidget

# Register your models here.
class PostAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = Post
        fields = '__all__'

admin.site.register(Post)
admin.site.register(Comment)