from django.db import models
from django.contrib.auth.models import User

class Movie(models.Model):
    title = models.CharField(max_length=150, unique=True)
    
    def __str__(self):
        return self.title

class Comment(models.Model):
    #each comment has a relationship to 1 movie and 1 user 
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(max_length=350)
    upvotes = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.content
