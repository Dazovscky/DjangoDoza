from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('process_letter/', views.letters_view, name='letters_view'),
    path('process_letter/<str:letter>/', views.process_letter, name='process_letter'),
    path('display_images/', views.display_images, name='display_images'),
    path('display_images/<str:list>/', views.display_images, name='display_images')
]
