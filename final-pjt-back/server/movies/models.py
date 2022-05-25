from django.db import models
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Genre(models.Model):
    name = models.TextField()

class Movie(models.Model):      
    title = models.TextField()
    original_title = models.TextField()
    overview = models.TextField()
    tagline = models.TextField()
    genres = models.ManyToManyField(Genre)
    poster_path = models.TextField()
    backdrop_path = models.TextField()
    vote_average = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(10)])
    vote_count = models.IntegerField(validators=[MinValueValidator(0)])
    release_date = models.TextField()
    runtime = models.IntegerField(validators=[MinValueValidator(0)])
    popularity = models.FloatField(validators=[MinValueValidator(0)])
    adult = models.BooleanField()
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="like_movies", symmetrical=True)
    watched_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="watched_movies", symmetrical=True)    
      
class Review(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField() 
    rank = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)])
    user =  models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="reviews")
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="like_reviews", symmetrical=True)
    movie =  models.ForeignKey(Movie, on_delete=models.CASCADE, related_name="reviews")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Comment(models.Model):    
    content = models.TextField() 
    user =  models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='comments')
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="like_comments", symmetrical=True)
    review =  models.ForeignKey(Review, on_delete=models.CASCADE, related_name="comments")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    

   