from django.db import models

class MyWatchList(models.Model):
    Watched = models.CharField(max_length=50)
    Title = models.TextField()
    Rating = models.IntegerField()
    Release_date = models.TextField()
    Review = models.TextField()
    
# Create your models here.
