from django.shortcuts import render

# Create your views here.
def gallery(request):
    return render(request, 'images/gallery.html')

def viewImage(request, pk):
    return render(request, 'images/image.html')

def addImage(request):
    return render(request, 'images/add_image.html')
