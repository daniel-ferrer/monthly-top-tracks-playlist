import spotipy

from spotipy.oauth2 import SpotifyOAuth

class SpotifyService:
    def __init__(self, client_id, client_secret, redirect_uri):
        self.client_id = client_id
        self.client_secret = client_secret
        self.redirect_uri = redirect_uri
        self.sp = None
    
    def authorize(self):
        sp_oauth = SpotifyOAuth(
            client_id=self.client_id,
            client_secret=self.client_secret,
            redirect_uri=self.redirect_uri,
            scope = "user-library-read user-top-read playlist-modify-public"
        )
        self.sp = spotipy.Spotify(auth_manager=sp_oauth)

    def get_top_tracks(self, limit=10, time_range="short_term"):
        top_tracks = self.sp.current_user_top_tracks(limit=limit, time_range=time_range)["items"]
        return [track for track in top_tracks]

    def create_playlist(self, playlist_name, description=None):
        playlists = self.sp.user_playlists(self.sp.me()["id"])
        existing_playlist = next((playlist for playlist in playlists["items"] if playlist["name"] == playlist_name), None)

        if existing_playlist:
            return existing_playlist["id"]
        
        new_playlist = self.sp.user_playlist_create(self.sp.me()["id"], playlist_name, description=description)
        return new_playlist["id"]
    
    def add_tracks_to_playlist(self, playlist_id, tracks):
        self.sp.playlist_add_items(playlist_id, [track["uri"] for track in tracks], position=None)