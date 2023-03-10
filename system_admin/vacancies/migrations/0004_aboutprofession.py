# Generated by Django 4.1.5 on 2023-01-14 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vacancies', '0003_delete_aboutprofession'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutProfession',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(null=True, verbose_name='Заголовок к тексту')),
                ('image', models.ImageField(default='', null=True, upload_to='images/%Y/%m/%d/', verbose_name='Изображения к тексту')),
                ('text', models.TextField(null=True, verbose_name='Текст описания')),
            ],
            options={
                'verbose_name': 'Описание профессии',
                'verbose_name_plural': 'Описание профессии',
            },
        ),
    ]
