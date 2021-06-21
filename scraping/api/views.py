import datetime
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .serializers import *


period = datetime.date.today()


class CityViewSet(ModelViewSet):
    """ Отображение доступных городов через api """
    queryset = City.objects.all()
    serializer_class = CitySerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class LanguageViewSet(ModelViewSet):
    """ Отображение доступных языков через api """
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class VacancyViewSet(ModelViewSet):
    """ Отображение вакансий через api """
    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        city_slug = self.request.query_params.get('city', None)
        lang_slug = self.request.query_params.get('lang', None)
        qs = None
        if city_slug and lang_slug:
            qs = Vacancy.objects.filter(city__slug=city_slug, language__slug=lang_slug, timestamp__gte=period)
            if not qs.exists():
                qs = Vacancy.objects.filter(city__slug=lang_slug, language__slug=city_slug, timestamp__gte=period)
        self.queryset = qs
        return self.queryset


