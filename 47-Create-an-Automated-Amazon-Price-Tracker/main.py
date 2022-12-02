from bs4 import BeautifulSoup
import requests
import pprint
import smtplib

import lxml

#Use item link to tap into the document of the page:
amazon_URL = "https://www.amazon.com/Instant-Pot-Pressure-Steamer-Sterilizer/dp/B08PQ2KWHS/ref=sr_1_2_sspa?crid=3PS0AQ9GG8NE&keywords=Instant+Pot+Duo+Evo&qid=1669968418&sprefix=instant+pot+duo+evo%2Caps%2C392&sr=8-2-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEyNTYzWU85WFJUQjlSJmVuY3J5cHRlZElkPUEwMTIwOTkxMVBCQU1GSlY0WkY5SSZlbmNyeXB0ZWRBZElkPUEwMzg0OTAxMk9aTTk5OTJORzU0NCZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU="
headers = {"Accept-Language": "en-US,en;q=0.9",
           "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"}
response = requests.get(amazon_URL, headers=headers)
# print(response.text)

#Use Beautifulsoup to make soup:

soup = BeautifulSoup(response.text, "lxml")
# pp = pprint.PrettyPrinter()
# pp.pprint(soup)

#Get hold of the price and convert that into an integer:
price_dollars = soup.find(name="span", class_="a-price-whole").getText()
print(price_dollars) #its a string
price_cents = soup.find(name="span", class_="a-price-fraction").getText()
print(price_cents) #its a string

#Calculate the actual price by adding the dollars and cents:
actual_price = float(price_dollars + price_cents)
print(actual_price)
print(type(actual_price))

