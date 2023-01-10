from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

navigation = [ 'Описание', 'Востребованность', 'География', 'Навыки', 'Недавние вакансии', ]

def index(request):
    return render(request, 'vacancies/index.html', { 'title': 'Системный-администратор', 'navigation': navigation, })

def demand(request):
    return render(request, 'vacancies/demand.html', { 'title': 'Востребованность', 'navigation': navigation, })

def geography(request):
    return render(request, 'vacancies/geography.html', { 'title': 'География', 'navigation': navigation, })

def skills(request):
    return render(request, 'vacancies/skills.html', { 'title': 'Навыки', 'navigation': navigation, })

def recent(request):
    return render(request, 'vacancies/recent.html', { 'title': 'Последние вакансии', 'navigation': navigation, })

def page_not_found(request, exception):
    return render(request, 'vacancies/notfound.html', { 'title': 'Страница не найдена', 'navigation': navigation, })