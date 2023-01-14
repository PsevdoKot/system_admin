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
    rows = SalaryInfoByYear.objects.all()
    graphs = SalaryInfoByYearGraph.objects.all()
    context = {
        'title': 'Востребованность',
        'headers': ['Год', 'Средняя зарплата', 'Средняя зарплата - системный администратор',
                    'Количество вакансий', 'Количество вакансий - системный администратор'],
        'rows': [[row.year, row.all_vac_level_statistics, row.slctd_vac_level_statistics,
                 row.all_vac_count_statistics, row.slctd_vac_count_statistics] for row in rows],
        'graph_urls': [graph.graph for graph in graphs],
    }
    return render(request, 'vacancies/demand.html', context=context)

def geography(request):
    rows1 = SalaryLevelByCity.objects.all()
    rows2 = SalaryCountByCity.objects.all()
    graphs = SalaryInfoByCityGraph.objects.all()
    context = {
        'title': 'География',
        'headers1': ['Город', 'Уровень зарплат'],
        'headers2': ['Город', 'Доля вакансий'],
        'rows1': [[row.city, row.all_vacancies_statistics] for row in rows1],
        'rows2': [[row.city, row.selected_vacancies_statistics] for row in rows2],
        'graph_urls': [graph.graph for graph in graphs],
    }
    return render(request, 'vacancies/geography.html', context=context)

def skills(request):
    rows = KeySkillsStatistics.objects.all()
    context = {
        'title': 'Навыки',
        'headers': ['Год', 'Топ-1', 'Топ-2', 'Топ-3', 'Топ-4', 'Топ-5', 'Топ-6', 'Топ-7', 'Топ-8', 'Топ-9', 'Топ-10'],
        'rows': [[row.year, row.key_skill_1, row.key_skill_2, row.key_skill_3, row.key_skill_4, row.key_skill_5,
                  row.key_skill_6, row.key_skill_7, row.key_skill_8, row.key_skill_9, row.key_skill_10] for row in rows],
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