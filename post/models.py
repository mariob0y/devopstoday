from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=120)
    link = models.URLField()
    date = models.DateField(auto_now=False, auto_now_add=True)
    author = models.CharField(max_length=50)
    upvote = models.IntegerField(default=0)
    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.PROTECT)
    author = models.CharField(max_length=50)
    content = models.TextField(max_length=1000)
    date = models.DateField(auto_now=False, auto_now_add=True)
    def __str__(self):
        return self.title