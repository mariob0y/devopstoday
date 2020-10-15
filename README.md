# devopstoday

## Start

1. Install requirements:
*  pip install -r requirements.txt
2. Run server:
* python manage.py runserver 

## API URLs 

* /api/posts - Create post, List all posts.
* /api/comments - Create comment, List all comments.
* /api/posts/<int:pk> - CRUD of single post.
* /api/comments/<int:pk> - CRUD of single comment.

(may be changed at post/urls.py)

## Functional Requirements Relization 

* Upvotes are limited to range (-10:10)
* Upvotes realized through views:
    posts/<int:id>/upvote 
    posts/<int:id>/downvote
* Upvote counters are set to zero every 24 hours, performed through APScheduler (zerocounter.py)
