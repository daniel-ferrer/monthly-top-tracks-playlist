import datetime

from decouple import config
from spotify_service import SpotifyService

if __name__ == "__main__":
    version = 1
    client_id = config('CLIENT_ID')
    client_secret = config('CLIENT_SECRET')
    redirect_uri = config('REDIRECT_URI')

    sp_service = SpotifyService(client_id, client_secret, redirect_uri)
    sp_service.authorize()

    top_tracks_4w = sp_service.get_top_tracks()
    top_10_tracks = sorted(top_tracks_4w, key=lambda x: x["popularity"], reverse=True)[:10]
    
    formatted_date = datetime.date.today().strftime("%m%Y")
    playlist_name = f'{formatted_date}.{version}'
    playlist_description = "Playlist created by https://github.com/daniel-ferrer/monthly-top-tracks-playlist"

    playlist_id = sp_service.create_playlist(playlist_name, playlist_description)

    sp_service.add_tracks_to_playlist(playlist_id, top_10_tracks)