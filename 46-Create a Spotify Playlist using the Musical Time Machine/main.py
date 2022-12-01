from bs4 import BeautifulSoup
import requests
import os

#Import class from spotify_suthentication.py:
from spotify_authentication import sp, user_id
# print(user_id)


#Take YYYY-MM-DD formatted date as input:
date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ") #enter 2012-11-09
#-----------------------------------------------------------------------------------------------------------------------------

#Get response from URL and print to see the format of the entire document:
response = requests.get("https://www.billboard.com/charts/hot-100/" + date) #becomes https://www.billboard.com/charts/hot-100/2012-11-09/
# print(response.text)
#-----------------------------------------------------------------------------------------------------------------------------

#Create soup object to get hold of the required info from the URL as a list:
soup = BeautifulSoup(response.text, 'html.parser')
song_names = soup.find_all(name="h3", id="title-of-a-story", class_="a-no-trucate")
# print(song_names)
#-----------------------------------------------------------------------------------------------------------------------------

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

song_urls = []
year = date.split("-")[0]
print(year)

#Create a list of song_urls:
song_urls = []
for song in final_song_list:
    # result = sp.search(q=f"track:{song} year:{year}", type="track")
    # print(f"track:{song} year:{year}")
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    # print(result["tracks"]["items"][0]["uri"])
    try:
        url = result["tracks"]["items"][0]["uri"]
        song_urls.append(url)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

print(song_urls)

#Create a playlist with a custom name:
playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
print(playlist)

#Add all items(urls) to playlist:
sp.playlist_add_items(playlist_id=playlist["id"], items=song_urls)







