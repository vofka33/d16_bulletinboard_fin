from django.forms import DateInput, SelectDateWidget
from django_filters import FilterSet, DateFilter, DateFromToRangeFilter
from django_filters.widgets import RangeWidget
from .models import Comment, Post
from django import forms


# class CommentFilter(FilterSet):
#     creation_date = DateFilter(field_name="creation_date", lookup_expr="gte", label="Дата от", widget=forms.DateInput(attrs={'type': 'date'}))
#
#     class Meta:
#         model = Comment
#         fields = {
#             'text': ['exact'],
#             'author': ['exact']
#         }


# class PostFilter(FilterSet):
#     creation_date = DateFilter(field_name="creation_date", lookup_expr="gte", label="Дата от", widget=forms.DateInput(attrs={'type': 'date'}))
#
#     class Meta:
#         model = Post
#         fields = {
#             'title': ['icontains'],
#             'author': ['exact'],
#             'category': ['exact']
#         }


class PostFilter(FilterSet):
    creation_date = DateFromToRangeFilter(label='Диапазон дат', widget=RangeWidget(attrs={'type': 'date'}))

    class Meta:
        model = Post
        fields = {
            'title': ['icontains'],
            'category': ['exact'],
        }


# class PostFilter(FilterSet):
#     data = DateFromToRangeFilter()
#
#     class Meta:
#         model = Post
#         fields = ['creation_date']