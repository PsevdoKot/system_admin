from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

def index(request):
    return HttpResponse('Системный-администратор')

def demand(request):
    return HttpResponse('Востребованность')

def geography(request):
    return HttpResponse('География')

def skills(request):
    return HttpResponse('Навыки')

def recent(request):
    return HttpResponse('Последние вакансии')

def page_not_found(request, exception):
    return HttpResponseNotFound('Страница не найдена')