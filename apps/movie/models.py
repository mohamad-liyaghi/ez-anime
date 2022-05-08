from django.db import models
from django.contrib.contenttypes.fields import GenericRelation
from star_ratings.models import Rating
from cast.models import Cast,Genre
# Create your models here.

class Film(models.Model):
    picture = models.ImageField(upload_to="Movie-images")
    name = models.CharField(max_length=20)
    intro = models.TextField()
    seoson_story = models.ManyToManyField("seoson",blank=True)
    imdb = models.PositiveIntegerField(default=0)
    seosons = models.PositiveIntegerField(default=0)
    actors= models.ManyToManyField(Cast,related_name='%(class)s_actor')
    director= models.ManyToManyField(Cast,related_name='%(class)s_director')
    ratings = GenericRelation(Rating, related_query_name='rate')
    release_date = models.DateField()
    def __str__(self) :
        return self.name

class seoson(models.Model):
    seoson_number = models.PositiveIntegerField(default=1)
    for_film = models.ForeignKey("Film",on_delete=models.CASCADE)
    story = models.TextField(null=True,blank=True)
    def __str__(self) -> str:
        return f'{self.seoson_number} | {self.for_film}'

