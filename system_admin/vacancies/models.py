from django.db import models

class Vacancy(models.Model):
    name = models.CharField(max_length=200)
    key_skills = models.TextField(null=True)
    salary_from = models.CharField(max_length=20)
    salary_to = models.CharField(max_length=20)
    area_name = models.CharField(max_length=50)
    published_at = models.DateTimeField()

class Recent_Vacancy(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True)
    key_skills = models.TextField(null=True)
    salary_from = models.CharField(max_length=20)
    salary_to = models.CharField(max_length=20)
    area_name = models.CharField(max_length=50)
    published_at = models.DateTimeField()

class Quote(models.Model):
    date = models.CharField(max_length=10)
    USD = models.FloatField(default=60.66)
    RUR = models.FloatField(default=1)
    EUR = models.FloatField(default=59.90)
    KZT = models.FloatField(default=0.13)
    UAH = models.FloatField(default=1.64)
    BYR = models.FloatField(default=23.91)

class About_Profession(models.Model):
    name = models.CharField(max_length=200)
    text = models.TextField(null=True)

class Salary_Info_By_Year(models.Model):
    year = models.SmallIntegerField()
    all_vac_level_statistics = models.IntegerField()
    slctd_vac_level_statistics = models.IntegerField()
    all_vac_count_statistics = models.IntegerField()
    slctd_vac_count_statistics = models.IntegerField()

class Salary_Level_By_City(models.Model):
    city = models.CharField(max_length=50)
    all_vacancies_statistics = models.IntegerField()

class Salary_Count_By_City(models.Model):
    city = models.CharField(max_length=50)
    selected_vacancies_statistics = models.CharField(max_length=20)

class Key_Skills_Statistics(models.Model):
    year = models.SmallIntegerField()
    key_skill_1 = models.CharField(max_length=50)
    key_skill_2 = models.CharField(max_length=50)
    key_skill_3 = models.CharField(max_length=50)
    key_skill_4 = models.CharField(max_length=50)
    key_skill_5 = models.CharField(max_length=50)
    key_skill_6 = models.CharField(max_length=50)
    key_skill_7 = models.CharField(max_length=50)
    key_skill_8 = models.CharField(max_length=50)
    key_skill_9 = models.CharField(max_length=50)
    key_skill_10 = models.CharField(max_length=50)
