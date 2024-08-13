import requests
import lxml
from bs4 import BeautifulSoup
import csv

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
    "Accept-Language": "en-US,en;q=0.5"
}

product_links = []
product_prices = []

with open("products.csv", encoding='utf-8-sig') as file:
    contents = csv.reader(file)
    for row in contents:
        product_links.append(row[0])
        product_prices.append(row[1])

for i in range(len(product_links)):
    response = requests.get(product_links[i], headers=headers)
    soup = BeautifulSoup(response.content, "lxml")
    pretty_soup = soup.prettify()
    print(pretty_soup)
    price_span = soup.find(name="span", class_="a-price-whole")
    price = int(price_span.getText().split('.')[0])
    if price < int(product_prices[i]):
        print(f"Might wanna buy the product: {product_links[i]}")
