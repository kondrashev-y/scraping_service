from django.contrib import admin
from django.urls import path, include

from scraping.views import home_view, VacancyView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),
    path('accounts/', include(('accounts.urls', 'accounts'))),
    path('vacancy/', VacancyView.as_view(), name='vacancy_list'),
]