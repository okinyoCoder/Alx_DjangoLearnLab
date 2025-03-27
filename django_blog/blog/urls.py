from django.urls import path, include
from .views import SignUpView
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView, LogoutView
from .views import *

urlpatterns = [
    path('',  include('django.contrib.auth.urls')),
    path('login/', LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='blog/logout.html'), name='logout'),
    path('profile/', TemplateView.as_view(template_name='blog/base.html'), name='profile'),
    path('register/', SignUpView.as_view(), name="blog/register"),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/', PostListView.as_view(), name='post-list'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('comment/new/', CommentCreateView.as_view(), name='create-comment'),
    path('comment/', CommentCreateList.as_view, name='all-comment'),
    path('comment/<int:pk>/', CommentDetailView.as_view(), name='detail-comment'),
    path('comment/<int:pk>/update/', CommentUpdateView.as_view, name='edit-comment'),
    path('comment/<int:pk>', CommentDeleteView.as_view, name='delete-comment'),
]