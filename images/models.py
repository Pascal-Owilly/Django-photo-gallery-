from django.db import models
from django.forms import CharField

# Create your models here.
class Category(models.Model):
    name = CharField(max_length=200)

    def __str__(self):
        return self.name


class Image(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    image = models.ImageField(null=False, blank=False)
    description = models.TextField()

    def __str__(self):
        return self.description
    