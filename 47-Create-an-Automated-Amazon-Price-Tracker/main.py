from bs4 import BeautifulSoup
import requests

#Use item link to tap into the document of the page:
amazon_URL = "https://www.amazon.com/Instant-Pot-Duo-Evo-Plus/dp/B07W55DDFB/ref=sr_1_1?qid=1597662463"
headers = {"Accept-Language": "en-US,en;q=0.9",
           "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"}
response = requests.get(amazon_URL, headers=headers)
print(response.text)


