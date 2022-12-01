from bs4 import BeautifulSoup
import requests

date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ") #enter 2012-11-09

response = requests.get("https://www.billboard.com/charts/hot-100/" + date) #becomes https://www.billboard.com/charts/hot-100/2012-11-09/
print(response.text)