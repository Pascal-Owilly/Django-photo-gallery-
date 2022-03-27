from unicodedata import name
from django.conf import settings
from django.urls import path
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.gallery, name='gallery'),
    path('image/<str:pk>', views.viewImage, name='image'),
    path('add_image/', views.addImage, name='add_image'),
    path('search/', views.search_results, name='search_results'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)


