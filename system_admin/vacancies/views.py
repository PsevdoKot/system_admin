from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from vacancies.models import *

def index(request):
    description = AboutProfession.objects.all()
    context = {
        'title': 'Системный-администратор',
        'description': description,
    }
    return render(request, 'vacancies/index.html', context=context)

def demand(request):
    description = AboutProfession.objects.all()
    context = {
        'title': 'Востребованность',
    }
    return render(request, 'vacancies/demand.html', context=context)

def geography(request):
    context = {
        'title': 'География',
    }
    return render(request, 'vacancies/geography.html', context=context)

def skills(request):
    context = {
        'title': 'Навыки',
    }
    return render(request, 'vacancies/skills.html', context=context)

def recent(request):
    context = {
        'title': 'Последние вакансии',
    }
    return render(request, 'vacancies/recent.html', context=context)

def page_not_found(request, exception):
    context = {
        'title': 'Страница не найдена',
        'content_title': 'Страницы с таким адресом не существует'
    }
    return render(request, 'vacancies/notfound.html', context=context)