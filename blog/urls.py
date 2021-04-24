from django.urls import path
from .views import (BlogListView, BlogCreateView, BlogEditView, BlogDeleteView, comment_list,
                    CommentListView, create_comment, post_details)

urlpatterns = [
    path('post/delete/<int:pk>/', BlogDeleteView.as_view(), name='post_delete'),
    path('post/edit/<int:pk>/', BlogEditView.as_view(), name='post_edit'),
    path('post/create/', BlogCreateView.as_view(), name='post_create'),
    path('post/<int:pk>/', post_details, name='post_detail'),
    path('post/<int:pk>/comment/create/', create_comment, name='create_comment'),
    path('post/<int:pk>/comments/', comment_list, name='comments'),
    path('', BlogListView.as_view(), name='home'),
]