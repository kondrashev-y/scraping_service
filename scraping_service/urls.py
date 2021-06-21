from django.contrib import admin
from django.urls import path, include

from scraping.views import home_view, VacancyView  # CreateVacancyView, UpdateVacancyView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),
    path('accounts/', include(('accounts.urls', 'accounts'))),
    path('vacancy/', VacancyView.as_view(), name='vacancy_list'),
    path('api/v1/', include(('scraping.api.urls', 'api'))),
    # path('create/', CreateVacancyView.as_view(), name='create_vacancy'),
    # path('update/<int:pk>/', UpdateVacancyView.as_view(), name='update_vacancy'),
]