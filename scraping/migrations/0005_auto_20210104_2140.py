# Generated by Django 3.1.4 on 2021-01-04 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scraping', '0004_urls'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='urls',
            options={'verbose_name': 'Адрес URL', 'verbose_name_plural': 'Адреса URL'},
        ),
        migrations.AlterModelOptions(
            name='vacancy',
            options={'ordering': ['-timestamp'], 'verbose_name': 'Вакансия', 'verbose_name_plural': 'Вакансии'},
        ),
        migrations.AlterField(
            model_name='error',
            name='timestamp',
            field=models.DateField(auto_now_add=True, verbose_name='Дата создания ошибки'),
        ),
    ]
