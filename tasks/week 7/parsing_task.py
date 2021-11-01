import requests
from decouple import config
from bs4 import BeautifulSoup
import csv

URL = "https://www.ikea.com/ru/ru/cat/divany-iz-kozhi-iskusstvennoy-kozhi-10662/"
HEADER = {
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36",
    "access": "*/*"
}
PATH = "sofa.csv"

def get_html(url, params = None):
    request = requests.get(url, headers=HEADER, params=params)
    return request

def get_content(html):
    soup = BeautifulSoup(html, "html.parser")
    items = soup.find_all("div", class_="plp-fragment-wrapper")
    books = []
    count = 1
    for item in items:
        x = [item.get_text() for item in soup.select("div.plp-availability-information")]
        books.append(
            {"title": item.find("div", class_="range-revamp-header-section__title--small notranslate").get_text(),
             "image": item.find("img").get("src"),
             "description": item.find("span", class_='range-revamp-header-section__description-text').get_text(),
             #"delivery": item.find("div", class_='plp-availability-information').span.get('p').get_text(),
             "delivery": x,
             "detail_product": item.find("a").get("href")
             }
        )
        count += 1
    return books

def save_csv(books, path):
    with open(path, "w") as f:
        writer = csv.writer(f, delimiter=";")
        writer.writerow(["Название", "Картинка", "Описание", "Доставка", "Ссылка на детализацию"])
        for book in books:
            writer.writerow([book["title"], book["image"], book["description"],
                            book["delivery"], book["detail_product"]
            ])

def parse():
    html = get_html(URL)
    if html.status_code == 200:
        electron_books = get_content(html.text)
        save_csv(electron_books, PATH)

parse()