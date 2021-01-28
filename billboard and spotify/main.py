from bs4 import BeautifulSoup
import requests
import lxml
import spotipy
from spotipy.oauth2 import SpotifyOAuth

year = input("Which year do you want to tavel to? Type de date in this format YYYY-MM-DD: ")

billboard_url = "https://www.billboard.com/charts/hot-100/" + year

response = requests.get(billboard_url)
billboard_web_page = response.text

soup = BeautifulSoup(billboard_web_page, parser="html.parser", features="lxml")

song_title_class = "chart-element__information__song text--truncate color--primary"

song_list = soup.find_all(name="span", class_=song_title_class)

song_titles = [song.getText() for song in song_list]

client_id = "your secret id"
client_secret = "your secret code"

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=client_id,
        client_secret=client_secret,
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id = sp.current_user()["id"]

songs_uri = []
for song in song_titles:
    results = sp.search(q='track: ' + song, type='track')
    try:
        songs_uri.append(results['tracks']['items'][0]['uri'])
    except IndexError:
        pass

print(f"{len(songs_uri)} has been added to the uri lists")


playlist_name = f"{year} Billboard 100"

new_playlist = sp.user_playlist_create(user=user_id, name=playlist_name, public=False, collaborative=False, description=f"top 100 songs on Billboard.com in {year}")
new_playlist_id = new_playlist['id']

sp.playlist_add_items(playlist_id=new_playlist_id, items=songs_uri, position=None)