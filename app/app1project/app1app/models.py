import self
from django.db import models

# Create your models here.
class Song(models.Model):
    song_name=models.CharField(max_length=200)
    movie_name=models.CharField(max_length=200)
    singer=models.CharField(max_length=200)
    year=models.IntegerField()
    img=models.ImageField(upload_to="gallery")
def __str__(self):
 return self.name

