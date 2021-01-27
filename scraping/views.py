from django.shortcuts import render
from django.urls import reverse_lazy

from .forms import FindForm, CreateVacancyForm
from .models import Vacancy, Language

from django.db.models import Count

from django.views import generic

import datetime


def new_vacancy_count():
    last_days = datetime.date.today()-datetime.timedelta(1)
    count_vacancy = Vacancy.objects.filter(timestamp__gte=last_days).values('language__name').annotate(Count('id'))
    return count_vacancy


def home_view(request):
    """Начальная страничкам"""
    form = FindForm()
    count_vacancy = new_vacancy_count()
    return render(request, 'scraping/home.html', {'form': form, 'count_vacancy': count_vacancy})


class VacancyView(generic.ListView):
    """Вывод списка вакансий"""
    model = Vacancy
    paginate_by = 10

    def get_queryset(self):
        city = self.request.GET.get('city')
        language = self.request.GET.get('language')
        _filter = {}
        if city or language:
            if city:
                _filter['city__slug'] = city
            if language:
                _filter['language__slug'] = language
        else:
            _filter['city__slug'] = city
        queryset = Vacancy.objects.filter(**_filter).select_related('city', 'language')
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = FindForm(self.request.GET)
        context['city'] = self.request.GET.get('city')
        context['language'] = self.request.GET.get('language')
        context['count_vacancy'] = new_vacancy_count()
        return context


# class CreateVacancyView(generic.CreateView):
#     model = Vacancy
#     form_class = CreateVacancyForm
#     template_name = 'scraping/create_vacancy.html'
#     success_url = reverse_lazy('home')


# class UpdateVacancyView(generic.UpdateView):
#     model = Vacancy
#     form_class = CreateVacancyForm
#     template_name = 'scraping/update_vacancy.html'
#     success_url = reverse_lazy('home')

