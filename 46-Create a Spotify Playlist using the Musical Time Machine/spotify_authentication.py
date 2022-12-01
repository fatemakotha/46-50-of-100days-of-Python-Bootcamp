import os

import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Spotify credentials:
ClientID = os.environ.get("ID")
ClientSecret = os.environ.get("Secret")

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=ClientID,
        client_secret=ClientSecret,
        show_dialog=True,
        cache_path="token.txt"
    )
)

user_id = sp.current_user()["id"]
print(user_id)

