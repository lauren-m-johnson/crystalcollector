from django.db import models

# Create your models here.
class Crystal(models.Model):
    name = models.CharField(max_length=50)
    hardness = models.IntegerField()
    structure = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    