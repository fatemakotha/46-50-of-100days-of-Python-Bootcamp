from bs4 import BeautifulSoup
import requests

# date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ") #enter 2012-11-09

response = requests.get("https://www.billboard.com/charts/hot-100/2012-11-09") #becomes https://www.billboard.com/charts/hot-100/2012-11-09/
# print(response.text)

soup = BeautifulSoup(response.text, 'html.parser')
song_names = soup.find_all(name="h3", id="title-of-a-story", class_="a-no-trucate")
print(song_names)

music_list = []
for song in song_names:
    text = song.getText()
    print(text)
    text = text.strip()
    print(text)
    music_list.append(text)
print(music_list)





