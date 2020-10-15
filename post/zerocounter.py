from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from .models import Post, Comment

def setzero():
    posts = Post.objects.all()
    posts.update(upvote=0)


def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(setzero, 'interval', hours=24)
    scheduler.start()
