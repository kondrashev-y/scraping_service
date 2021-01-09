from django.core.paginator import Paginator
from django.db.models import Q
from django.db.models.query import QuerySet
from django.shortcuts import render

from .forms import FindForm
from .models import Vacancy, City

from django.views import generic


def home_view(request):
    """Начальная страничкам"""
    form = FindForm()
    return render(request, 'scraping/home.html', {'form': form})


def list_view(request):
    """Вывод вакансий"""
    city = request.GET.get('city')
    language = request.GET.get('language')
    form = FindForm()
    context = {'city': city, 'language': language, 'form': form}
    # page_obj = []
    if city or language:
        _filter = {}
        if city:
            _filter['city__slug'] = city
        if language:
            _filter['language__slug'] = language
        qs = Vacancy.objects.filter(**_filter)
        paginator = Paginator(qs, 10)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context['object_list'] = page_obj
    # else:
    #     qs = Vacancy.objects.all()
    return render(request, 'scraping/list.html', context)


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
        # queryset = Vacancy.objects.filter(
        #     Q(city__slug=self.request.GET.get('city')),
        #     Q(language__slug=self.request.GET.get('language'))
        # )
        queryset = Vacancy.objects.filter(**_filter)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = FindForm(self.request.GET)
        context['city'] = self.request.GET.get('city')
        context['language'] = self.request.GET.get('language')
        return context
