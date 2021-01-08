import requests
import codecs
from bs4 import BeautifulSoup as BS


headers = {'User-Agent':'Mozilla/5.0 (Windows NT 5.1; rv:47.0) Gecko/20100101 Firefox/47.0',
           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'}

url = 'https://www.superjob.ru/vacancy/search/?keywords=Python&geo%5Bt%5D%5B0%5D=4'
resp = requests.get(url, headers=headers)

jobs = []
errors = []
domain = 'https://www.superjob.ru'

if resp.status_code == 200:
    soup = BS(resp.content, 'html.parser')
    main_div = soup.find('div', attrs={'class': '_3Qutk'})
    if main_div:
        # div_list = main_div.find_all('div', attrs={'data-qa': 'vacancy-serp__vacancy'})
        div_list = main_div.find_all('div', attrs={'class': 'f-test-vacancy-item'})
        for div in div_list:
            # title = div.find('a', attrs={'data-qa': 'vacancy-serp__vacancy-title'})
            # title = div.find('span', attrs={'class': '_3mfro PlM3e _2JVkc _3LJqf'})
            title = div.find('a')
            href = title['href']
            pl = div.find('span', attrs={'class': 'f-test-text-company-item-location'})
            place = pl.find_all('span')[2].text
            company = div.find('span', attrs={'class': 'f-test-text-vacancy-item-company-name'})
            description = div.find('span', attrs={'_3mfro _38T7m _9fXTd _2JVkc _2VHxz _15msI'}).text
            salary = div.find('span', attrs={'class': '_3mfro _2Wp8I PlM3e _2JVkc _2VHxz'})
            if salary:
                salary = salary.text
            else:
                salary = ''
            jobs.append({
                'title': title.text, 'url': domain + href,
                'salary': salary, 'place': place,
                'company': company, 'description': description,
            })
        else:
            errors.append({'url': url, 'title': 'Div dose not exist'})
    else:
        errors.append({'url': url, 'title': 'Page do not response'})
for i in jobs:
    print(i)


h = codecs.open('work2.txt', 'w', 'utf-8')
h.write(str(jobs))
h.close()