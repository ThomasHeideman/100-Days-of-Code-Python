import requests
import urllib3
from datetime import datetime
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
import os

# 1. Setup & Environment
load_dotenv()
scope = "playlist-modify-private"

# Fetching credentials from .env
SPOTIPY_CLIENT_ID = os.getenv("SPOTIPY_ID")
SPOTIPY_CLIENT_SECRET = os.getenv("SPOTIPY_SECRET")
SPOTIPY_REDIRECT_URI = os.getenv("SPOTIPY_REDIRECT_URI")

# Suppress SSL warnings due to verify=False
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# 2. User Input & Date Conversion
date_input = input("Which year do you want to travel to? Type the date in this format DD-MM-YYYY: ")
header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:149.0) Gecko/20100101 Firefox/149.0"}

# Note: Your code uses %d-%m-%Y based on the previous error, matching your input '24-04-1990'
date_object = datetime.strptime(date_input, "%d-%m-%Y")

year = date_object.isocalendar()[0]
week = date_object.isocalendar()[1]

# 3. Scraping Top 40
url = f"https://www.top40.nl/top40/{year}/week-{week}"
response = requests.get(url, headers=header, verify=False)
response.encoding = "utf-8"
soup = BeautifulSoup(response.text, "html.parser")

listings = soup.find_all(name="div", class_="top40-list__item")
song_data = []

for listing in listings:
    title_el = listing.select_one("h2.h3")
    artist_el = listing.select_one("h3.p.lead.lowercase")

    if title_el and artist_el:
        song_data.append({
            "title": title_el.get_text().strip(),
            "artist": artist_el.get_text().strip(),
        })

print(f"Scraped {len(song_data)} songs from the charts.")

# 4. Spotify Authentication & Search
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    scope=scope,
    show_dialog=True,
    cache_path="token.txt"
))

user_id = sp.current_user()["id"]
print(f"Success! Logged in as user ID: {user_id}")

uri_list = []
playlist_name = f"Top40_{year}_Week_{week}"

print("Searching for tracks on Spotify...")
for song in song_data:
    # Constructing query
    query = f"track:{song['title']} artist:{song['artist']}"
    try:
        sp_response = sp.search(q=query, limit=1, type='track')
        tracks = sp_response['tracks']['items']
        if tracks:
            uri = tracks[0]['uri']
            uri_list.append(uri)
            print(f"Found: {song['title']}")
        else:
            print(f"Not found on Spotify: {song['title']}")
    except Exception as e:
        print(f"Error searching for {song['title']}: {e}")

# 5. Local Save (Bypassing Premium restriction for Playlist Creation)
print(f"\nDone! Total URIs collected: {len(uri_list)}")

with open("playlist_uris.txt", "w") as file:
    for uri in uri_list:
        file.write(f"{uri}\n")

print(f"\n--- REPORT ---")
print(f"Due to Spotify Premium restrictions, tracks have been saved locally.")
print(f"Number of songs found for {year}: {len(uri_list)}")
print(f"URIs are exported to 'playlist_uris.txt'.")

# Optional: Uncomment to create Spotify Playlist - requires Spotify Premium
# new_playlist = sp.user_playlist_create(user_id, playlist_name, public=False)
# sp.playlist_add_items(new_playlist["id"], uri_list)