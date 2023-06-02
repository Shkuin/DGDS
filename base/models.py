from django.db import models

# Create your models here.
class Game(models.Model):
    name = models.CharField(max_length=100)
    genre = models.CharField(max_length=200)
    description = models.TextField()
    platform = models.CharField(max_length=100)
    poster = models.CharField(max_length=1000)
    images = models.JSONField() # it's gonna store like a json, we will convert it to python list
    price = models.FloatField()
    token_id = models.CharField(max_length=100)
    private_key = models.CharField(max_length=200)

    def __str__(self):
        return self.name