from django.db import models

class MyWatchList(models.Model):
    Watched = models.BooleanField()
    Title = models.CharField(max_length=255, default='')
    Rating = models.IntegerField()
    Release_date = models.TextField()
    Review = models.TextField()
    
# Create your models here.
