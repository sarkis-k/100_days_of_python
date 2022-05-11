import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth
from keys import *
import re

# first time use only. to get the auth bearer
# auth_manager = SpotifyClientCredentials(client_id=spotify_id, client_secret=spotify_key)
# sp = spotipy.Spotify(auth_manager=auth_manager)
# playlists = sp.current_user()
# print(playlists)

# use it after you got .cache file
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri=spotify_redirect,
        client_id=spotify_id,
        client_secret=spotify_key,
        show_dialog=True,
        cache_path=".cache"
    ))

user_id = sp.current_user()["id"]

date = input("enter date: ")

website = requests.get(f"https://www.billboard.com/charts/hot-100/{date}/").text

soup = BeautifulSoup(website, "html.parser")
song_chart = soup.find_all(name="div", class_="chart-results-list")
# print(song_chart)
song_names_spans = soup.find_all(name="h3",
                                 id="title-of-a-story")  # , class_="c-title a-no-trucate a-font-primary-bold-s")
song_names_dirty = [song.getText() for song in song_names_spans]
song_names = []
for x in song_names_dirty:
    w = re.split(r"\W+", x)
    j = " ".join(w)
    song_names.append(j)

song_uris = []
year = date.split("-")[0]
for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")
        pass


playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)

sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)

