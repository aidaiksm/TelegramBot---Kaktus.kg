from bs4 import BeautifulSoup
import requests
import lxml

url = 'https://kaktus.media/?date=2020-12-01&lable=8&order=main#paginator'
HEADERS = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
           'User-Agent':
           'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:83.0) Gecko/20100101 Firefox/83.0'
           }

def get_html(url, params=''):
    response = requests.get(url, headers=HEADERS, params=params)
    return response
   

def get_content(html, num):
    soup = BeautifulSoup(html, features='lxml')
    section = soup.find('ul', class_='topic_list')
    items = section.find_all('div', class_='t f_medium')
    title_list = []

    for item in items[:20]:
        title = item.find('span', class_='n').text
        title_list.append(title)  
    if num != 0:
        return title_list[num-1]
    i = 0
    line = ''
    for name in title_list:
        i = 1 + i
        line = line + str(i) + ')' + name + '\n'
    return line




html = get_html(url)

