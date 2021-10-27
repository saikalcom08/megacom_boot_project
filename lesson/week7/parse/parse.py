import requests
from decouple import config
from bs4 import BeautifulSoup
import csv

URL = "https://www.kivano.kg/planshety-i-bukridery"
HEADER = {
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36",
    "access": "*/*"
}
LINK = "https://www.kivano.kg"
PATH = "planshet.csv"

def get_html(url, params = None):
    request = requests.get(url, headers=HEADER, params=params)
    return request

def get_content(html):
    soup = BeautifulSoup(html, "html.parser")
    items = soup.find_all("div", class_="item product_listbox oh")
    books = []
    count = 1
    for item in items:
        x = item.find("div", class_="listbox_title oh").get_text().replace("\n", "")
        y = item.find("div", class_="listbox_price text-center").findChild("strong").get_text().replace("\n", "").replace(" сом", "")
        books.append(
            {"title": item.find("div", class_="listbox_title oh").get_text().replace("\n", ""),
             "image": LINK + item.find("img").get("src"),
             "description": item.find("div", class_='product_text pull-left').get_text().replace(f"{x}", ""),
             "price": y + " (som)",
             "detail_product": LINK + item.find("a").get("href"),
             "item": count,
             "converted_price": str(round((int(y) / 85), 1)) + " (usd)"
             }
        )
        count += 1
    return books

def save_csv(books, path):
    with open(path, "w") as f:
        writer = csv.writer(f, delimiter=";")
        writer.writerow(["Номер", "Название планшета", "Цена в сомах", "Цена в долларах", "Описание", "Картинка", "Ссылка на детализацию"])
        for book in books:
            writer.writerow([book["item"], book["title"], book["price"], book["converted_price"],
                             book["description"], book["image"], book["detail_product"]
            ])

def parse():
    html = get_html(URL)
    if html.status_code == 200:
        electron_books = get_content(html.text)
        save_csv(electron_books, PATH)

parse()