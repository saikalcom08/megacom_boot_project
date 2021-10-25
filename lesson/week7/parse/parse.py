import requests
from decouple import config
from bs4 import BeautifulSoup

URL = "https://www.kivano.kg/planshety-i-bukridery"
HEADER = {
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36",
    "access": "*/*"
}
LINK = "https://www.kivano.kg"
def get_html(url, params = None):
    request = requests.get(url, headers=HEADER, params=params)
    return request

def get_content(html):
    soup = BeautifulSoup(html, "html.parser")
    items = soup.find_all("div", class_="item product_listbox oh")
    book = []
    for item in items:
        book.append(
            {"title": item.find("div", class_="listbox_title oh").get_text().replace("\n", ""),
             "image": LINK + item.find("img").get("src"),
             "description": item.find("div", {'class': 'listbox_title oh'}).get_text(),
             "price": item.find("div", class_="listbox_price text-center").get_text().replace("\n", "")
             }
        )
    print(book)

def parse():
    html = get_html(URL)
    if html.status_code == 200:
        get_content(html.text)

parse()