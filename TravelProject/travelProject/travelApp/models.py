from django.db import models

# Create your models here.
class Places(models.Model):
    place = models.CharField(max_length=250)
    img = models.ImageField(upload_to='pics')
    description = models.TextField()

    def __str__(self):
        return self.place

class Team(models.Model):
    name = models.CharField(max_length=250)
    desc = models.TextField()
    img = models.ImageField(upload_to='pics')

    def __str__(self):
        return self.name