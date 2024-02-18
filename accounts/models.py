from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser
class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    watched_movies = models.ManyToManyField('Movie', related_name='watched_by', blank=True)

    def __str__(self):
        return self.user.username
class Movie(models.Model):
    movie_id = models.CharField(max_length=50)
    title = models.CharField(max_length=100)
    year = models.IntegerField()

    def __str__(self):
        return self.title+" "+str(self.year)
class CustomUser(AbstractUser):
    pass