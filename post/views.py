from django.shortcuts import render

# Create your views here.

from django.shortcuts import redirect
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView

class PostCreate(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class CommentCreate(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class SinglePostView(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class SingleCommentView(RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

def PostList(request):
    queryset = Post.objects.all()
    context = {"object_list": queryset}
    return render(request, "posts.html", context)

def PostView(request, id=None):
    post = Post.objects.get(id=id)
    comments = Comment.objects.filter(post=id)
    context = {"post": post, "comments" : comments}
    return render(request, "post_view.html", context)

def PostUpvote(request, id=None):
    post = Post.objects.get(id=id)
    if post.upvote <= 9:
        post.upvote = post.upvote + 1
        post.save()
        return redirect('/allposts')
    else:
        post.upvote = 10
        post.save()
        return redirect('/allposts')

def PostDownvote(request, id=None):
    post = Post.objects.get(id=id)
    if post.upvote >= -9:
        post.upvote = post.upvote - 1
        post.save()
        return redirect('/allposts')
    else:
        post.upvote = -10
        post.save()
        return redirect('/allposts')

