from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('', views.gallery, name='gallery'),
    path('image/<str:pk>', views.viewImage, name='image'),
    path('add_image/', views.addImage, name='add_image'),
    # path('delete_image/', views.deleteImage, name='delete_image'),
]
