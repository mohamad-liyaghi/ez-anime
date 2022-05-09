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
    full_name = models.CharField(max_length=50,null=True)
    biography = models.TextField()
    birthday  = models.DateField()
    genre = models.ManyToManyField(Genre,blank=True)
    works =models.ForeignKey(to="movie.Film",on_delete=models.CASCADE,blank=True,null=True)
    role = models.CharField(max_length=1, choices=role.choices,default=role.actor)
    def __str__(self):
        return self.full_name
        


