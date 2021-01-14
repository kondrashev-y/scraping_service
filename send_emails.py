import os, sys
import django
import datetime
from django.core.mail import EmailMultiAlternatives

from django.contrib.auth import get_user_model

proj = os.path.dirname(os.path.abspath('manage.py'))
sys.path.append(proj)
os.environ['DJANGO_SETTINGS_MODULE'] = "scraping_service.settings"

django.setup()

from scraping.models import Vacancy, Error, Urls, City, Language
from scraping_service.settings import EMAIL_HOST_USER
from django.utils import timezone


today = datetime.date.today()
# today = timezone.now()
subject = f'Рассылка вакансий за {today}'
text_content = f'Рассылка вакансий {today}'
from_email = EMAIL_HOST_USER
ADMIN_USER = EMAIL_HOST_USER
empty = f'<h2>За {today} по вашим параметрам нет новых вакансий!</h2>'
User = get_user_model()
qs = User.objects.filter(send_email=True).values('city', 'language', 'email')
users_dct = {}
for i in qs:
    users_dct.setdefault((i['city'], i['language']), [])
    users_dct[(i['city'], i['language'])].append(i['email'])
if users_dct:
    params = {'city_id__in': [], 'language_id__in': []}
    for pair in users_dct.keys():
        params['city_id__in'].append(pair[0])
        params['language_id__in'].append(pair[1])
    qs = Vacancy.objects.filter(**params, timestamp=today).values()
    vacancies = {}
    for i in qs:
        vacancies.setdefault((i['city_id'], i['language_id']), [])
        vacancies[(i['city_id'], i['language_id'])].append(i)
    for keys, emails in users_dct.items():
        rows = vacancies.get(keys, [])
        html = ''
        for row in rows:
            html += f'<h3><a href="{ row["url"] }">{ row["title"] }</a></h3>'
            html += f'<h5>{ row["company"] }</h5>'
            html += f'<p class="card-text">{ row["description"] }</p><br><hr>'
        _html = html if html else empty
        for email in emails:
            to = email
            print('to', to)
            msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
            msg.attach_alternative(_html, "text/html")
            msg.send()


qs = Error.objects.filter(timestamp=today)
subject = ''
text_content = ''
content = ''
if qs.exists():
    error = qs.first()
    data = error.data.get('errors', [])
    for i in data:
        content += f'<p><a href="{ i["url"] }">Error: { i["title"] }</a></p>'
    subject = f'Ошибки скрапинга {today}'
    text_content = 'Ошибки скрапинга'
    data = error.data.get('user_data')
    if data:
        content += '<hr>'
        content += '<h2> Пожелания пользователей </h2>'
    for i in data:
        content += f'<p>Город: {i["city"]}, Язык: {i["language"]}, Email: {i["email"]}</a></p>'
    subject = f'Пожелания пользователей {today}'
    text_content = 'Пожелания пользователей'

qs = Urls.objects.all().values('city', 'language')
city = City.objects.all().values('name', 'id')
city_dct = {i['id']: i['name'] for i in city}
language = Language.objects.all().values('name', 'id')
language_dct = {i['id']: i['name'] for i in language}
urls_dct = {(i['city'], i['language']): True for i in qs}
urls_errors = ''
for keys in users_dct.keys():
    if keys not in urls_dct:
        if keys[0] and keys[1]:
            urls_errors += f'<p> Для города { city_dct[keys[0]] } и языка { language_dct[keys[1]]  } отсутствует url</p>'
            subject += 'Отсутсвтующие урлы'
            content += urls_errors

if subject:
    msg = EmailMultiAlternatives(subject, text_content, from_email, [ADMIN_USER])
    msg.attach_alternative(content, "text/html")
    msg.send()


