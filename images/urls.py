from django.urls import path
from . import views

urlpatterns = [
    path('', views.gallery, name='gallery')
    path('image/<str:pk>', views.views.viewImage, name='image'),
    path('addImage', views.add_image, name='addImage'),
]           