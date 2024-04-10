from unittest import loader
from django.shortcuts import render
from django.http import HttpResponse
from .models import *


def index(request):
    latest_question_list = Case.objects.all()
    context = {"latest_question_list": latest_question_list}
    return render(request, "galery/gallery.html", context)


def letters_view(request):
    letters = [chr(i) for i in range(ord('А'), ord('Я') + 1)]
    return render(request, 'galery/gallery.html', {'letters': letters})


def process_letter(request, letter):
    filtered_cases = Case.objects.filter(name__istartswith=letter)
    list_author = list(filtered_cases.values_list('name', flat=True))
    return render(request, 'galery/gallery.html', {'cases': list_author})



