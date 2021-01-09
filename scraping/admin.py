from django.contrib import admin

from .models import City, Language, Vacancy, Error, Urls

admin.site.register(City)
admin.site.register(Language)
# admin.site.register(Vacancy)
admin.site.register(Error)
admin.site.register(Urls)

@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    """Вакансии"""
    list_display = ("title", "url", "salary", "timestamp")
    # list_display_links = ("url",)