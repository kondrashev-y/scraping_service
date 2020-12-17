from django.shortcuts import render
from .models import Vacancy


def home_view(request):
    city = request.GET.get('city')
    language = request.GET.get('language')
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
    return render(request, 'scraping/home.html', {'object_list': qs})
