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

class PostAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'creation_date', 'category', 'author')
    list_filter = ('title', 'creation_date', 'category', 'author')
    search_fields = ('title', 'creation_date', 'category', 'author')


class CommentAdmin(admin.ModelAdmin):
    list_display = ('pk', 'creation_date', 'accepted', 'author', 'post')
    list_filter = ('creation_date', 'accepted', 'author')
    search_fields = ('creation_date', 'accepted', 'author')


admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)