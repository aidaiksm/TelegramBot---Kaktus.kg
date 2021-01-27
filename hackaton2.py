from bs4 import BeautifulSoup
import requests
import lxml


def get_news():
    headers = {"User-Agent":"Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11"}
    response = requests.get('https://kaktus.media/?date=2020-12-06&lable=8&order=main#paginator', headers=headers)
    soup = BeautifulSoup(response.content, "lxml")
    return soup


def get_links(*num):
    links = get_news().find_all("div", class_="t f_medium")
    urls = []
    for link in links[:20]:
        url = link.find("a").get("href")
        urls.append(url)

    print(urls)

get_links()