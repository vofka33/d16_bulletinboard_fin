from django.contrib import admin
from django.urls import path, include
from .views import PostsList, PostDetailView, PostAddView, CommentAddView, PostDeleteView, PostEditView, CommentsModeratonView
from . import views

# , PostDeleteView, SearchList, EditUserProfile, CategoryList
# from django.contrib.auth.views import LoginView, LogoutView
# from .views import upgrade_me, add_subscribe

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


   # path('user_update/', EditUserProfile.as_view(), name='user_update'),
   # # path('login/', LoginView.as_view(template_name='news/login.html'), name='login'),
   # # path('logout/', LogoutView.as_view(template_name='news/logout.html'), name='logout'),
   # path('accounts/', include('allauth.urls')),
   # path('upgrade/', upgrade_me, name='upgrade'),
   # path('category/', CategoryList.as_view(), name='category'),
   # path('<int:pk>/add_subscribe', add_subscribe, name='subscribe'),
   # path('', IndexView.as_view()),
   ]