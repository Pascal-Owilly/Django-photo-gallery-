from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=150, null=False, blank=False)

    def __str__(self):
        return self.name
    class Meta:
        ordering = ['name']


class Image(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    image = models.ImageField(null=False, blank=False)
    description = models.TextField()
    

    def __str__(self):
        return self.description

class Location(models.Model):
    locality = models.TextField()

    def __str__(self):
        return self.locality
    