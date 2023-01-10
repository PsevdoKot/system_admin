from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

def index(request):
    return render(request, 'Системный-администратор')

def demand(request):
    return render(request, 'Востребованность')

def geography(request):
    return render(request, 'География')

def skills(request):
    return render(request, 'Навыки')

def recent(request):
    return render(request, 'Последние вакансии')

def page_not_found(request, exception):
    return render(request, 'Страница не найдена')