from django.contrib import admin
from django.urls import path

from scraping.views import home_view, list_view, VacancyView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),
    path('list/', list_view, name='list'),
    path('vacancy/', VacancyView.as_view(), name='vacancy_list'),
]