from django.db import models
# Create your models here.

class Genre(models.Model):
    title = models.CharField(max_length=20)
    films_related = models.ManyToManyField(to="movie.Film",related_name="movie_genre",blank=True)
    def __str__(self) :
        return self.title

class Cast(models.Model):
    class role(models.TextChoices):
        actor = "a"
        director = "d"
    avatar = models.ImageField(upload_to="actors/")
    full_name = models.CharField(max_length=50,null=True)
    biography = models.TextField()
    birthday  = models.DateField()
    genre = models.ManyToManyField(Genre,blank=True)
    works =models.ManyToManyField(to="movie.Film",blank=True)
    role = models.CharField(max_length=1, choices=role.choices,default=role.actor)
    def __str__(self):
        return self.full_name
        


