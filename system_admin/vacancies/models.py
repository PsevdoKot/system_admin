from django.db import models

class Vacancy(models.Model):
    name = models.CharField(max_length=200)
    key_skills = models.TextField(null=True)
    salary_from = models.CharField(max_length=20)
    salary_to = models.CharField(max_length=20)
    area_name = models.CharField(max_length=80)
    published_at = models.DateTimeField()

class Recent_Vacancy(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True)
    key_skills = models.TextField(null=True)
    salary_from = models.CharField(max_length=20)
    salary_to = models.CharField(max_length=20)
    area_name = models.CharField(max_length=80)
    published_at = models.DateTimeField()

class Quote(models.Model):
    date = models.SmallIntegerField()
    USD = models.FloatField(default=60.66)
    RUR = models.FloatField(default=1)
    EUR = models.FloatField(default=59.90)
    KZT = models.FloatField(default=0.13)
    UAH = models.FloatField(default=1.64)
    BYR = models.FloatField(default=23.91)
