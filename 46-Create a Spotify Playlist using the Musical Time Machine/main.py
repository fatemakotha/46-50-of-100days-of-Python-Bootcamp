from bs4 import BeautifulSoup
import requests
import os

#Take YYYY-MM-DD formatted date as input:
date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ") #enter 2012-11-09

response = requests.get("https://www.billboard.com/charts/hot-100/" + date) #becomes https://www.billboard.com/charts/hot-100/2012-11-09/
# print(response.text)

soup = BeautifulSoup(response.text, 'html.parser')
song_names = soup.find_all(name="h3", id="title-of-a-story", class_="a-no-trucate")
# print(song_names)


#Create list of songs from URL:
final_song_list = []
for song in song_names:
    text = song.getText()
    # print(text)
    text = text.strip()
    # print(text)
    final_song_list.append(text)
print(final_song_list)
#-----------------------------------------------------------------------------------------------------------------------------

# Spotify credentials:
ClientID = os.environ.get("ID")
ClientSecret = os.environ.get("Secret")






