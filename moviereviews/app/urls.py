from django.urls import path

from moviereviews.app.api import userView
from moviereviews.app.api import commentView
from moviereviews.app.api import movieView

urlpatterns = [
    path('users/home', userView.get_home),
    path('users/get', userView.get_all_users),
    path('users/get/user', userView.get_user),
    path('user/create', userView.create_user),
    path('comments/get/movie', commentView.get_comments_for_movie),
    path('comments/get/user', commentView.get_comments_for_user),
    path('comments/update/upvotes', commentView.update_upvote_count),
    path('comments/create', commentView.create_comment),
    path('movies/create', movieView.create_movie) 
]