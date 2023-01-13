from django.contrib import admin

from .models import *


class RecentVacancyAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'key_skills', 'salary', 'area_name', 'published_at')
    search_fields = ('name', 'key_skills', 'area_name')
    list_display_links = ('name', )

class AboutProfessionAdmin(admin.ModelAdmin):
    list_display = ('title', 'text')
    list_display_links = ('title', 'text')

class SalaryInfoByYearAdmin(admin.ModelAdmin):
    list_display = ('year', 'all_vac_level_statistics', 'slctd_vac_level_statistics',
                    'all_vac_count_statistics', 'slctd_vac_count_statistics')
    search_fields = ('year', )
    list_display_links = ('year', )

class SalaryLevelByCityAdmin(admin.ModelAdmin):
    list_display = ('city', 'all_vacancies_statistics')
    search_fields = ('city', )
    list_display_links = ('city', )

class SalaryCountByCityAdmin(admin.ModelAdmin):
    list_display = ('city', 'selected_vacancies_statistics')
    search_fields = ('city', )
    list_display_links = ('city', )

class KeySkillsStatisticsAdmin(admin.ModelAdmin):
    list_display = ('year', 'key_skill_1', 'key_skill_2', 'key_skill_3', 'key_skill_4', 'key_skill_5',
                    'key_skill_6', 'key_skill_7', 'key_skill_8', 'key_skill_9', 'key_skill_10', )
    search_fields = ('key_skill_1', 'key_skill_2', 'key_skill_3', 'key_skill_4', 'key_skill_5',
                    'key_skill_6', 'key_skill_7', 'key_skill_8', 'key_skill_9', 'key_skill_10')
    list_display_links = ('year', )

admin.site.register(RecentVacancy, RecentVacancyAdmin)
admin.site.register(AboutProfession, AboutProfessionAdmin)
admin.site.register(SalaryInfoByYear, SalaryInfoByYearAdmin)
admin.site.register(SalaryLevelByCity, SalaryLevelByCityAdmin)
admin.site.register(SalaryCountByCity, SalaryCountByCityAdmin)
admin.site.register(KeySkillsStatistics, KeySkillsStatisticsAdmin)
