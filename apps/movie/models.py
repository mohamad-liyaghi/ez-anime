from django.db import models
from django.contrib.contenttypes.fields import GenericRelation
from star_ratings.models import Rating
from element.models import Cast,Genre
# Create your models here.

class Film(models.Model):
    picture = models.ImageField(upload_to="Movie-images")
    name = models.CharField(max_length=20)
    intro = models.TextField()
    imdb = models.PositiveIntegerField(default=0)
    actors= models.ManyToManyField(Cast, related_name='movie_actor',blank=True)
    director= models.ManyToManyField(Cast, related_name='movie_director',blank=True)
    genre= models.ManyToManyField(Genre, related_name='movie_genre', blank=True)
    ratings = GenericRelation(Rating, related_query_name='rate')
    release_date = models.DateField()
    token = models.CharField(max_length=15,unique=True,null=True,blank=True)
    views = models.ManyToManyField("View", blank=True)
    def __str__(self) :
        return self.name
    
        

class Season(models.Model):
    '''Season model for series'''

    number = models.PositiveIntegerField(default=1)
    film = models.ForeignKey("Film", blank=True, on_delete=models.CASCADE, related_name="seasons")
    story = models.TextField(null=True,blank=True)
    token = models.CharField(max_length=10, blank=True)

    def __str__(self) -> str:
        return f'{str(self.number)} | {self.film}'


class View(models.Model):
    user_ip = models.GenericIPAddressField()
    def __str__(self) -> str:
        return self.user_ip
