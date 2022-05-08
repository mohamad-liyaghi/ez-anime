from django.db import models
# Create your models here.

class Genre(models.Model):
    title = models.CharField(max_length=20)
    films_related = models.ForeignKey(to="movie.Film",on_delete=models.CASCADE,blank=True,null=True)
    def __str__(self) :
        return self.title

class Cast(models.Model):
    class role(models.TextChoices):
        actor = "a"
        director = "d"
    avatar = models.ImageField(upload_to="actors/")
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    biography = models.TextField()
    birthday  = models.DateField()
    genre = models.ManyToManyField(Genre)
    works =models.ForeignKey(to="movie.Film",on_delete=models.CASCADE,blank=True,null=True)
    role = models.CharField(max_length=1, choices=role.choices,default=role.actor)
    def __str__(self):
        return self.first_name+" "+self.last_name
        


