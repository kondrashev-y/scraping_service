import codecs
import os, sys
from django.db import DatabaseError

proj = os.path.dirname(os.path.abspath('manage.py'))
sys.path.append(proj)
os.environ['DJANGO_SETTINGS_MODULE'] = "scraping_service.settings"

import django
django.setup()

from scraping.models import Vacancy, City, Language
from scraping.parser import *


parsers = (
    (for_hh, 'https://hh.ru/search/vacancy?clusters=true&area=1&enable_snippets=true&salary=&st=searchVacancy&text=Python'),
    (for_superjob, 'https://www.superjob.ru/vacancy/search/?keywords=Python&geo%5Bt%5D%5B0%5D=4'),
    (for_rabota, 'https://www.rabota.ru/vacancy/?query=python&sort=relevance'),
)

city = City.objects.filter(slug='moscow').first()
language = Language.objects.filter(slug='python').first()

jobs, errors = [], []

for fun, url in parsers:
    j, e = fun(url)
    jobs += j
    errors += e

for job in jobs:
    v = Vacancy(**job, city=city, language=language)
    try:
        v.save()
    except DatabaseError:
        pass

# h = codecs.open('work.txt', 'w', 'utf-8')
# h.write(str(jobs))
# h.close()
