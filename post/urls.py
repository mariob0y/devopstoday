from django.urls import path

from .views import PostCreate, CommentCreate, SinglePostView, SingleCommentView



urlpatterns = [
    path('posts', PostCreate.as_view() ),
    path('comments', CommentCreate.as_view() ),
    path('posts/<int:pk>', SinglePostView.as_view()),
    path('comments/<int:pk>', SingleCommentView.as_view()),
    
]