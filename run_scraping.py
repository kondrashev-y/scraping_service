import codecs
import os, sys
import asyncio
import datetime

from django.contrib.auth import get_user_model
from django.db import DatabaseError

proj = os.path.dirname(os.path.abspath('manage.py'))
sys.path.append(proj)
os.environ['DJANGO_SETTINGS_MODULE'] = "scraping_service.settings"

import django

django.setup()

from scraping.models import Vacancy, City, Language, Error, Urls
from scraping.parser import *

User = get_user_model()

parsers = (
    (for_hh, 'hh'),
    (for_superjob, 'superjob'),
    (for_rabota, 'rabota'),
)

jobs, errors = [], []


def get_settings():
    qs = User.objects.filter(send_email=True).values()
    settings_lst = set((q['city_id'], q['language_id']) for q in qs)
    return settings_lst


def get_urls(_settings):
    qs = Urls.objects.all().values()
    url_dict = {(q['city_id'], q['language_id']): q['url_data'] for q in qs}
    urls = []
    for pair in _settings:
        if pair in url_dict:
            tmp = {}
            tmp['city'] = pair[0]
            tmp['language'] = pair[1]
            tmp['url_data'] = url_dict[pair]
            urls.append(tmp)
    return urls


async def main(value):
    func, url, city, language = value
    job, err = await loop.run_in_executor(None, func, url, city, language)
    jobs.extend(job)
    errors.extend(err)


settings = get_settings()
url_list = get_urls(settings)

# city = City.objects.filter(slug='moscow').first()
# language = Language.objects.filter(slug='python').first()

loop = asyncio.get_event_loop()
tmp_tasks = [(func, data['url_data'][key], data['city'], data['language'])
             for data in url_list
             for func, key in parsers]
if tmp_tasks:
    tasks = asyncio.wait([loop.create_task(main(f)) for f in tmp_tasks])
    loop.run_until_complete(tasks)
    loop.close()


# for data in url_list:
#     for fun, key in parsers:
#         url = data['url_data'][key]
#         j, e = fun(url, city=data['city'], language=data['language'])
#         jobs += j
#         errors += e


for job in jobs:
    v = Vacancy(**job)
    try:
        v.save()
    except DatabaseError:
        pass

if errors:
    qs = Error.objects.filter(timestamp=datetime.date.today())
    if qs.exists():
        er = qs.first()
        er.data.update({'errors': errors})
        er.save()
    else:
        err = Error(data=f'errors:{errors}').save()

# h = codecs.open('work.txt', 'w', 'utf-8')
# h.write(str(jobs))
# h.close()


ten_days_ago = datetime.date.today() - datetime.timedelta(10)
Vacancy.objects.filter(timestamp__lte=ten_days_ago).delete()