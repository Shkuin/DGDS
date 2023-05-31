from django.db import models

# Create your models here.
class Game(models.Model):
    name = models.CharField(max_length=100)
    json = models.JSONField(max_length=5000)
    private_key = models.CharField(max_length=200)

    def __str__(self):
        return self.name