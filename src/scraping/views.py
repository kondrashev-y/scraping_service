from django.shortcuts import render

from .forms import FindForm
from .models import Vacancy


def home_view(request):
    """Вывод вакансий"""
    city = request.GET.get('city')
    language = request.GET.get('language')
    form = FindForm()
    qs = []
    if city or language:
        _filter = {}
        if city:
            _filter['city__slug'] = city
        if language:
            _filter['language__slug'] = language
        qs = Vacancy.objects.filter(**_filter)
    else:
        qs = Vacancy.objects.all()
    return render(request, 'scraping/home.html', {'object_list': qs, 'form': form})
