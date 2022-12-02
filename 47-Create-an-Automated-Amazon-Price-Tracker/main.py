import os

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

#Get hold of the name/title of the item:
title = soup.find(name="span", id="productTitle", class_="a-size-large product-title-word-break").getText()
title.strip()
print(title)

#Get hold of the price and convert that into an integer:
price_dollars = soup.find(name="span", class_="a-price-whole").getText()
# print(price_dollars) #its a string
price_cents = soup.find(name="span", class_="a-price-fraction").getText()
# print(price_cents) #its a string


#Calculate the actual price by adding the dollars and cents:
actual_price = float(price_dollars + price_cents)
print(actual_price)
print(type(actual_price))

#Set email ID and password:
my_email = os.environ.get("EMAIL")
my_app_pass = os.environ.get("PASSWORD")
# print(my_email)
# print(my_app_pass)

#Set BUY price:
BUY_PRICE = 200

# Set loop so that when price is lower than BUY_PRICE an email is sent out:
if actual_price < BUY_PRICE:
    message = f"{title} is now {actual_price}"
    print("HELLO")
    print(message)
    title = title.encode('utf-8')
    with smtplib.SMTP_SSL("smtp.gmail.com", port=465) as connection:
        connection.ehlo()
        connection.login(user=my_email, password=my_app_pass)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="fatema.alam.kotha@gmail.com",
            msg=f"The price is for {title} is now {actual_price}"
        )
        connection.close()
