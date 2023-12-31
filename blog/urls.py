# from django.contrib import admin
from django.urls import path
from . views import (PostListView,
                    PostDetailView,
                    PostCreateView,
                    PostUpdateView,
                    PostDeleteView,
                    UserPostListView
                    )

from . import views

    

# by importing the ListView 

# this include function will include

urlpatterns = [
    path('', views.index, name='index'),
    path('post/<int:post_id>/add_comment/', views.add_comment, name='add-comment'),
    path('home/', PostListView.as_view(), name='blog-home'),
    path('user/<str:username>',UserPostListView.as_view(),name='user-posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name='post-delete'),
    path('about/', views.about, name='blog-about'),
     path('my-blogs/', views.my_blogs, name='my-blogs'),
    
    path('post/<int:post_id>/reply_comment/<int:parent_id>/', views.reply_comment, name='reply-comment'),
   

]
