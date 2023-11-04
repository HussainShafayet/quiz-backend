from django.urls import path
from . import views

urlpatterns = [
    path('imagepost/', views.handleImage, name='handleImage'),
    path('imagedelete/', views.handleImageDelete, name='handleImageDelete'),
]



