from django.urls import path
from . import views

urlpatterns = [
    path('process_letter/', views.letters_view, name='letters_view'),
    path('process_letter/<str:letter>/', views.process_letter, name='process_letter'),
]
