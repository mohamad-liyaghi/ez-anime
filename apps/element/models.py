from django.db import models


class Genre(models.Model):
    title = models.CharField(max_length=120)

    def __str__(self) :
        return self.title


class Cast(models.Model):

    class role(models.TextChoices):
        actor = "a"
        director = "d"

    avatar = models.ImageField(upload_to="actors/")
    full_name = models.CharField(max_length=50, null=True)

    biography = models.TextField()
    birthday  = models.DateField()

    role = models.CharField(max_length=1, choices=role.choices,default=role.actor)
    token = models.CharField(max_length=10,blank=True)

    def __str__(self):
        return self.full_name


class Tag(models.Model):
    title = models.CharField(max_length=120)
        
    def __str__(self):
        return self.title