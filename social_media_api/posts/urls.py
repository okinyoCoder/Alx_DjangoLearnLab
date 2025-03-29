from . import views
from django.urls import path
from.views import *

urlpatterns = [
    path('posts/', views.view_post, name='posts'),
    path('post/new', views.create_post, name='create_post'),
    path('post/<int:pk>/', views.view_post, name='post_detail'),
    path('post/<int:pk>/update', views.update_post, name='update_post'),
    path('post/<int:pk>/delete', views.delete_post, name='delete_post'),
        path('post/<int:pk>/comments/new/',
         CommentCreateView.as_view(), name='create_comment'),
    path('post/<int:pk>/comments/',
         CommentListView.as_view(), name='list_comment'),
    path('comment/<int:pk>/update/',
         CommentUpdateView.as_view(), name='update_comment'),
    path('comment/<int:pk>/delete/',
         CommentDeleteView.as_view(), name='delete_comment'),
    path('comment/<int:pk>/',
         CommentDetailView.as_view(), name='view_comment'),
]