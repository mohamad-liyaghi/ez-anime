from django.db import models
from django.contrib.contenttypes.fields import GenericRelation
from star_ratings.models import Rating
from cast.models import Cast,Genre
# Create your models here.

class Film(models.Model):
    picture = models.ImageField(upload_to="Movie-images")
    name = models.CharField(max_length=20)
    intro = models.TextField()
    seoson_story = models.ManyToManyField("season",blank=True)
    imdb = models.PositiveIntegerField(default=0)
    seosons = models.PositiveIntegerField(default=0)
    actors= models.ManyToManyField(Cast,related_name='%(class)s_actor',blank=True)
    director= models.ManyToManyField(Cast,related_name='%(class)s_director',blank=True)
    genre= models.ManyToManyField(Genre,related_name='%(class)s_genre',blank=True)
    ratings = GenericRelation(Rating, related_query_name='rate')
    release_date = models.DateField()
    token = models.CharField(max_length=15,unique=True,null=True,blank=True)
    def __str__(self) :
        return self.name
    
        

class season(models.Model):
    season_number = models.PositiveIntegerField(default=1)
    for_film = models.ManyToManyField("Film",blank=True)
    story = models.TextField(null=True,blank=True)
    token = models.CharField(max_length=10, blank=True)
    def __str__(self) -> str:
        return f'{self.season_number} | {self.for_film.first()}'

