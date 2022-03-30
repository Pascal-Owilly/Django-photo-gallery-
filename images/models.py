from django.db import models
from cloudinary.models import CloudinaryField
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=150, null=False, blank=False)
   
    def __str__(self):
        return self.name
    class Meta:     
        ordering = ['name']

class Article(models.Model):
    category = models.CharField(max_length=60)
    @classmethod
    def search_by_category(cls,search_term):
        results = cls.objects.filter(category__icontains=search_term)

class Image(models.Model):
    
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    image = CloudinaryField('image')
    description = models.TextField()


    def delete(self):
        return self.delete == False
        self.save()


    def __str__(self):
        return self.description

class Location(models.Model):
    locality = models.TextField()
    def __str__(self):
        return self.locality
    