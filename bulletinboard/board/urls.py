from django.contrib import admin
from django.urls import path, include
from .views import PostsList, PostDetailView, PostAddView, CommentAddView, PostDeleteView, PostEditView, CommentsModeratonView
from . import views

urlpatterns = [
   path('', PostsList.as_view()),
   path('<int:pk>/', PostDetailView.as_view(), name='post_detail'),
   path('add/', PostAddView.as_view(), name='post_add'),
   path('<int:pk>/add_comment/', CommentAddView.as_view(), name='add_comment'),
   path('<int:pk>/edit', PostEditView.as_view(), name='post_edit'),
   path('<int:pk>/delete', PostDeleteView.as_view(), name='post_delete'),
   path('moderation/', CommentsModeratonView.as_view(), name='comment_moderation'),
   path('comment/<int:pk>/accept/', views.comment_accept, name='comment_accept'),
   path('comment/<int:pk>/reject/', views.comment_reject, name='comment_reject'),
   path('comment/<int:pk>/remove/', views.comment_remove, name='comment_remove'),
   ]

