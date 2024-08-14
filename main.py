from selenium import webdriver
from selenium.webdriver.common.by import By
import csv
import time
import smtplib
from email.message import EmailMessage
import os
from dotenv import load_dotenv

load_dotenv()
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--no-sandbox")
# chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")
browser = webdriver.Chrome(options=chrome_options)
gmail_password = os.environ.get("GMAIL_PASSWORD")

product_links = []
product_prices = []

# email setup
s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
# Authentication
s.login("julian.costinea@gmail.com", gmail_password)
# Create a MIME text object
msg = EmailMessage()
msg['From'] = "julian.costinea@gmail.com"
msg['To'] = "emil.costinea@gmail.com"
msg['Subject'] = 'Consider buying this product'

with open("products.csv", encoding='utf-8-sig') as file:
    contents = csv.reader(file)
    for row in contents:
        product_links.append(row[0])
        product_prices.append(row[1])

for i in range(len(product_links)):
    browser.get(product_links[i])
    time.sleep(5)
    price = int(browser.find_element(By.CLASS_NAME, "a-price-whole").text)
    if price < int(product_prices[i]):
        msg.set_content(f"Product link: {product_links[i]}")
        s.send_message(msg)
