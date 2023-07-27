from django.db import models
from django.urls import reverse

# Create your models here.
class Crystal(models.Model):
    name = models.CharField(max_length=50)
    hardness = models.IntegerField()
    structure = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    transparency = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'crystal_id': self.id})
    