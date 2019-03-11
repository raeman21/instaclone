from django.db import models

# Create your models here.

class Image(models.Model):
    image_name = models.CharField(max_length=30)
    image_caption = models.TextField()
    profile = models.ForeignKey(profile)
    likes = models.IntegerField()
    comments = models.TextField()