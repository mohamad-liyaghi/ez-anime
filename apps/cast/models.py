from django.db import models

# Create your models here.

class Genre(models.Model):
    title = models.CharField(max_length=20)
    # films = models.ForeignKey()

class Cast(models.Model):
    class role(models.TextChoices):
        actor = "a"
        director = "d"
    avatar = models.ImageField(upload_to="actors/")
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    biography = models.TextField()
    birthday  = models.DateField()
    # works = models.ForeignKey()
    role = models.CharField(max_length=1, choices=role.choices,default=role.actor)
    


