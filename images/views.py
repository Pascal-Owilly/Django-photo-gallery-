from django.shortcuts import render
from .models import Category, Image

# Create your views here.
def gallery(request):
    categories = Category.objects.all()
    context = {'categories' : categories}
    return render(request, 'images/gallery.html', context)

def viewImage(request, pk):
    return render(request, 'images/image.html')

def addImage(request):
    return render(request, 'images/add_image.html')
