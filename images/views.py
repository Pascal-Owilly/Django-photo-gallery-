from django.shortcuts import render
from .models import Category, Image

# Create your views here.
def gallery(request):
    categories = Category.objects.all()
    images = Image.objects.all()
    context = {'categories' : categories, 'images' : images}
    return render(request, 'images/gallery.html', context)

def viewImage(request, pk):
    image  = Image.objects.get(id=pk)
    return render(request, 'images/image.html', {'image' : image})

def addImage(request):
    categories = Category.objects.all()

    if request.method == 'POST':
        data = request.POST
        image = request.FILES.get('image')

        print('data:', data)
        print('image:', image)


    context = {'categories' : categories}
    return render(request, 'images/add_image.html', context)
 
    