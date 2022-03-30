
from django.shortcuts import render, redirect
from .models import Category, Image
from django.views.decorators.csrf import csrf_exempt
from .models import Article

# Create your views here.

def search_results(request):

    if 'article' in request.GET and request.GET["article"]:
        search_term = request.GET.get("article")
        searched_articles = Article.search_by_category(search_term)
        message = f"{search_term}"

        return render(request, 'search_results.html',{"message":message,"images": searched_articles})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-news/search.html',{"message":message})

def delete_photo(request, id):
    image = Image.objects.get(pk=id)
    image.delete()==False
    return redirect('gallery')



def gallery(request):
    category = request.GET.get('category')

    if category == None:
          images = Image.objects.all()

    else:
        images = Image.objects.filter(category__name=category)
    categories = Category.objects.all()
    context = {'categories' : categories, 'images' : images}
    return render(request, 'images/gallery.html', context)
@csrf_exempt
def viewImage(request, pk):
    image  = Image.objects.get(id=pk)
    return render(request, 'images/image.html', {'image' : image})

def addImage(request):
    categories = Category.objects.all()

    if request.method == 'POST':
        data = request.POST
        image = request.FILES.get('image')

        if data['category'] != 'none':
            category = Category.objects.get(id=data['category'])

        elif data['new_category'] != '':
              category, created = Category.objects.get_or_create(name=data['new_category'])
        else:
            category = None

        image = Image.objects.create(
            category=category,
            description=data['description'],
            image=image,
        ) 

        return redirect('gallery')
    context = {'categories' : categories}
    return render(request, 'images/add_image.html', context)
 
    