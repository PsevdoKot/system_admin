from django.db import models


class RecentVacancy(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название', )
    description = models.TextField(null=True, verbose_name='Описание', )
    key_skills = models.TextField(null=True, verbose_name='Навыки', )
    salary = models.CharField(max_length=20, verbose_name='Оклад', )
    area_name = models.CharField(max_length=50, verbose_name='Название города', )
    published_at = models.DateTimeField(verbose_name='Дата публикации', )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Недавняя вакансия'
        verbose_name_plural = 'Недавние вакансии'

class AboutProfession(models.Model):
    title = models.TextField(null=True, verbose_name='Заголовок к тексту', )
    text = models.TextField(null=True, verbose_name='Текст описания', )

    def __str__(self):
        return 'Описание профессии'

    class Meta:
        verbose_name = 'Описание профессии'
        verbose_name_plural = 'Описание профессии'

class SalaryInfoByYear(models.Model):
    year = models.SmallIntegerField(verbose_name='Год', )
    all_vac_level_statistics = models.IntegerField(verbose_name='Уровень зарплат для всех профессий', )
    slctd_vac_level_statistics = models.IntegerField(verbose_name='Уровень зарплат для выбранной профессии', )
    all_vac_count_statistics = models.IntegerField(verbose_name='Количество вакансий для всех профессий', )
    slctd_vac_count_statistics = models.IntegerField(verbose_name='Количество вакансий для выбранной профессии', )

    def __str__(self):
        return self.year

    class Meta:
        verbose_name = 'Статистика по годам'
        verbose_name_plural = 'Статистика по годам'

class SalaryLevelByCity(models.Model):
    city = models.CharField(max_length=50, verbose_name='Город', )
    all_vacancies_statistics = models.IntegerField(verbose_name='Уровень зарплат для всех профессий', )

    def __str__(self):
        return self.city

    class Meta:
        verbose_name = 'Уровень зарплат вакансий по городам'
        verbose_name_plural = 'Уровни зарплат вакансий по городам'

class SalaryCountByCity(models.Model):
    city = models.CharField(max_length=50, verbose_name='Город', )
    selected_vacancies_statistics = models.CharField(max_length=20, verbose_name='Количество вакансий для выбранной профессии', )

    def __str__(self):
        return self.city

    class Meta:
        verbose_name = 'Число вакансий по городам'
        verbose_name_plural = 'Число вакансий по городам'

class KeySkillsStatistics(models.Model):
    year = models.SmallIntegerField()
    key_skill_1 = models.CharField(max_length=50, verbose_name='Топ 1', )
    key_skill_2 = models.CharField(max_length=50, verbose_name='Топ 2', )
    key_skill_3 = models.CharField(max_length=50, verbose_name='Топ 3', )
    key_skill_4 = models.CharField(max_length=50, verbose_name='Топ 4', )
    key_skill_5 = models.CharField(max_length=50, verbose_name='Топ 5', )
    key_skill_6 = models.CharField(max_length=50, verbose_name='Топ 6', )
    key_skill_7 = models.CharField(max_length=50, verbose_name='Топ 7', )
    key_skill_8 = models.CharField(max_length=50, verbose_name='Топ 8', )
    key_skill_9 = models.CharField(max_length=50, verbose_name='Топ 9', )
    key_skill_10 = models.CharField(max_length=50, verbose_name='Топ 10', )

    def __str__(self):
        return self.year

    class Meta:
        verbose_name = 'Популярные навыки'
        verbose_name_plural = 'Популярные навыки'
