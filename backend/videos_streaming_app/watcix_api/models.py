from django.db import models

# Create your models here.


class Movie(models.Model):
    Uploader_name = models.CharField(max_length=50)
    Name_of_movie = models.CharField(max_length=50)
    Genre_of_movie = models.TextField()
    Duration_of_movie = models.IntegerField(default=1000)
    Rating = models.IntegerField(default=10)
    Thumbnail = models.ImageField(upload_to='movies/Images')
    Video_clip = models.FileField(upload_to='movies')
