from unittest import loader
from django.shortcuts import render
from django.http import HttpResponse
from .models import *


def index(request):
    latest_question_list = Case.objects.all()
    context = {"latest_question_list": latest_question_list}
    return render(request, "galery/base.html", context)


def letters_view(request):
    letters = [chr(i) for i in range(ord('А'), ord('Я') + 1)]
    return render(request, 'galery/base.html', {'letters': letters})


def process_letter(request, letter):
    filtered_cases = Case.objects.filter(name__istartswith=letter)
    list_author = filtered_cases.values_list('name', flat=True)
    return render(request, 'galery/base.html', {'list_author': list_author})


def display_images(request, list):
    cases_img = Case.objects.get(name=list)
    case_id = cases_img.id
    images = CaseFile.objects.filter(case_id=case_id)
    return render(request, 'galery/base.html', {'cases_img': cases_img, 'images': images})


def choise_case(request, id):
    pass
