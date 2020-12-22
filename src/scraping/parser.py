import requests
import codecs
from bs4 import BeautifulSoup as BS
from random import randint


__all__ = ('for_hh', 'for_superjob', 'for_rabota')

headers = [
    {'User-Agent': 'Mozilla/5.0 (Windows NT 5.1; rv:47.0) Gecko/20100101 Firefox/47.0',
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'},
    {'User-Agent': 'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) '
                   'Chrome/49.0.2623.112 Safari/537.36',
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'},
    {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:53.0) Gecko/20100101 Firefox/53.0',
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'},
    {'User-Agent': 'Mozilla/5.0 (X11; OpenBSD i386) AppleWebKit/537.36 (KHTML, like Gecko) '
                   'Chrome/36.0.1985.125 Safari/537.36'},
    {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X x.y; rv:42.0) Gecko/20100101 Firefox/42.0'}

    ]
url = 'https://hh.ru/search/vacancy?clusters=true&area=1&enable_snippets=true&salary=&st=searchVacancy&text=Python'
# domain = 'https://hh.ru'


def for_hh(url):
    """Парсер сайта hh.ru"""
    jobs = []
    errors = []
    resp = requests.get(url, headers=headers[randint(0, 4)])
    if resp.status_code == 200:
        soup = BS(resp.content, 'html.parser')
        main_div = soup.find('div', attrs={'class': 'vacancy-serp'})
        if main_div:
            # div_list = main_div.find_all('div', attrs={'data-qa': 'vacancy-serp__vacancy'})
            div_list = main_div.find_all('div', attrs={'class': 'vacancy-serp-item'})
            for div in div_list:
                # title = div.find('a', attrs={'data-qa': 'vacancy-serp__vacancy-title'})
                title = div.find('span', attrs={'class': 'g-user-content'})
                href = title.a['href']
                place = div.find('span', attrs={'data-qa': 'vacancy-serp__vacancy-address'}).text
                company = div.find('div', attrs={'class': 'vacancy-serp-item__meta-info-company'}).text
                description = div.find('div', attrs={'g-user-content'}).text
                salary = div.find('span', attrs={'data-qa': 'vacancy-serp__vacancy-compensation'})
                if salary:
                    salary = salary.text
                else:
                    salary = 'По договоренности'
                jobs.append({
                    'title': title.text, 'url': href,
                    'salary': salary, 'company': company, 'description': description,
                })
            else:
                errors.append({'url': url, 'title': 'Div dose not exist'})
        else:
            errors.append({'url': url, 'title': 'Page do not response'})
    # for i in jobs:
    #     print(i[title], i[salary])
    return jobs, errors


def for_superjob(url):
    """Парсер сайта superjob.ru"""
    jobs = []
    errors = []
    domain = 'https://www.superjob.ru'
    resp = requests.get(url, headers=headers[randint(0, 4)])

    if resp.status_code == 200:
        soup = BS(resp.content, 'html.parser')
        main_div = soup.find('div', attrs={'class': '_1ID8B'})
        if main_div:
            div_list = main_div.find_all('div', attrs={'class': 'f-test-vacancy-item'})
            for div in div_list:
                title = div.find('a')
                href = title['href']
                pl = div.find('span', attrs={'class': 'f-test-text-company-item-location'})
                place = pl.find_all('span')[2].text
                company = div.find('span', attrs={'class': 'f-test-text-vacancy-item-company-name'}).text
                description = div.find('span', attrs={'_3mfro _38T7m _9fXTd _2JVkc _2VHxz _15msI'}).text
                salary = div.find('span', attrs={'class': '_3mfro _2Wp8I PlM3e _2JVkc _2VHxz'})
                if salary:
                    salary = salary.text
                else:
                    salary = ''
                jobs.append({
                    'title': title.text, 'url': domain + href,
                    'salary': salary, 'company': company, 'description': description,
                })
            else:
                errors.append({'url': url, 'title': 'Div dose not exist'})
        else:
            errors.append({'url': url, 'title': 'Page do not response'})
    return jobs, errors


def for_rabota(url):
    """Парсер сайта rabota.ru"""
    jobs = []
    errors = []
    domain = 'https://www.rabota.ru'
    resp = requests.get(url, headers=headers[randint(0, 4)])

    if resp.status_code == 200:
        soup = BS(resp.content, 'html.parser')
        # main_div = soup.find('main', attrs={'class': 'vacancy-search-page__main'})
        main_div = soup.find('div', attrs={'class': 'r-serp__infinity-list'})
        if main_div:
            div_list = main_div.find_all('div', attrs={'class': 'vacancy-preview-card__top'})
            for div in div_list:
                title = div.find('h3', attrs={'class': 'vacancy-preview-card__title'})
                href = title.a['href']
                place = div.find('span', attrs={'class': 'vacancy-preview-location__address-text'})
                company = div.find('span', attrs={'class': 'vacancy-preview-card__company-name'})
                description = div.find('div', attrs={'vacancy-preview-card__content'}).text
                if not description:
                    description = 'Нет информации'
                salary = div.find('div', attrs={'class': 'vacancy-preview-card__salary'})
                if salary:
                    salary = salary.text
                else:
                    salary = ''
                jobs.append({
                    'title': title.text.strip(), 'url': domain + href,
                    'salary': salary, 'company': company.text, 'description': description,
                })
            else:
                errors.append({'url': url, 'title': 'Div dose not exist'})
        else:
            errors.append({'url': url, 'title': 'Page do not response'})
    return jobs, errors


if __name__ == '__main__':
    url = 'https://www.superjob.ru/vacancy/search/?keywords=Python&geo%5Bt%5D%5B0%5D=4'
    # url = 'https://www.rabota.ru/vacancy/?query=python&sort=relevance'
    jobs, errors = for_superjob(url)
    # h = codecs.open('work.html', 'w', 'utf-8')
    # h.write(str(resp.text))
    h = codecs.open('work.txt', 'w', 'utf-8')
    h.write(str(jobs))
    h.close()