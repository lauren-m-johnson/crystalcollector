from django.db import models
from django.urls import reverse

# Create your models here.
class Prop(models.Model):
    property = models.CharField(max_length=50)
    
    def __str__(self):
        return self.property
    
    def get_absolute_url(self):
        return reverse("props_detail", kwargs={"pk": self.id})
    
class Crystal(models.Model):
    name = models.CharField(max_length=50)
    hardness = models.IntegerField()
    structure = models.CharField(max_length=50)
    color = models.CharField(max_length=100)
    transparency = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'crystal_id': self.id})
    
class Aquired(models.Model):
    date = models.DateField('Date Aquired')
    location = models.CharField(max_length=50)

    crystal = models.ForeignKey(Crystal, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.location} on {self.date}"
    
    class Meta:
        ordering = ['-date']