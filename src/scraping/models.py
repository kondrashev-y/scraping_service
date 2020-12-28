from django.db import models
import jsonfield

from .utils import for_cyrillic_to_eng


def default_url():
    return {'hh': '', 'superjob': '', 'rabota': ''}


class City(models.Model):
    """Города"""
    name = models.CharField(max_length=100, verbose_name='Название города', unique=True)
    slug = models.CharField(max_length=100, blank=True, unique=True)

    class Meta:
        verbose_name = 'Название города'
        verbose_name_plural = 'Названия городов'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = for_cyrillic_to_eng(str(self.name))
        super().save(*args, **kwargs)


class Language(models.Model):
    """Языки программирования"""
    name = models.CharField(max_length=100, verbose_name='Язык программирования', unique=True)
    slug = models.CharField(max_length=100, blank=True, unique=True)

    class Meta:
        verbose_name = 'Язык программирования'
        verbose_name_plural = 'Языки программирования'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = for_cyrillic_to_eng(str(self.name))
        super().save(*args, **kwargs)


class Vacancy(models.Model):
    """Вакансии"""
    url = models.URLField(unique=True)
    title = models.CharField(max_length=255, verbose_name='Заголовок вакансии')
    company = models.CharField(max_length=255, verbose_name='Компания')
    description = models.TextField(verbose_name='Описание вакансии')
    city = models.ForeignKey('City', verbose_name='Город', on_delete=models.CASCADE)
    language = models.ForeignKey('Language', verbose_name='Язык программирования', on_delete=models.CASCADE)
    timestamp = models.DateField(auto_now_add=True, verbose_name='Дата создания вакансии')
    # salary = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Зарплата')
    salary = models.CharField(max_length=50, verbose_name='Зарплата')

    class Meta:
        verbose_name = 'Вакансия'
        verbose_name_plural = 'Вакансии'
        ordering = ['-timestamp']

    def __str__(self):
        return self.title


class Error(models.Model):
    """Ошибки при скрапинге"""
    timestamp = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания ошибки')
    data = jsonfield.JSONField()
    
    class Meta:
        verbose_name = 'Ошибка'
        verbose_name_plural = 'Ошибки'


class Urls(models.Model):
    """Адреса для скрапинга"""
    city = models.ForeignKey('City', verbose_name='Город', on_delete=models.CASCADE)
    language = models.ForeignKey('Language', verbose_name='Язык программирования', on_delete=models.CASCADE)
    url_data = jsonfield.JSONField(default=default_url)
    
    class Meta:
        unique_together = ('city', 'language')
        verbose_name = 'Адрес URL'
        verbose_name_plural = 'Адреса URL'


            