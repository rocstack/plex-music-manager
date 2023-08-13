from flask import Flask, jsonify, request, redirect, session
from flask_cors import CORS
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from flask_session import Session

app = Flask(__name__)
CORS(app)
app.config['SECRET_KEY'] = 'supersecretsessionkey'
app.config['SESSION_TYPE'] = 'filesystem'  # Use filesystem session
Session(app)

SPOTIPY_CLIENT_ID = ''
SPOTIPY_CLIENT_SECRET = ''
SPOTIPY_REDIRECT_URI = 'http://localhost:5173/spotify/callback'
SCOPE = 'user-library-read playlist-read-private playlist-read-collaborative playlist-modify-public playlist-modify-private'

sp_oauth = SpotifyOAuth(client_id=SPOTIPY_CLIENT_ID, client_secret=SPOTIPY_CLIENT_SECRET, redirect_uri=SPOTIPY_REDIRECT_URI, scope=SCOPE)


@app.route('/')
def plex_music_manager():
    return jsonify(message="plex_music_manager")


@app.route('/spotify/login', methods=['GET'])
def spotify_login():
    auth_url = sp_oauth.get_authorize_url()
    return jsonify({'auth_url': auth_url})


@app.route('/spotify/callback', methods=['GET'])
def spotify_callback():
    token_info = sp_oauth.get_access_token(request.args['code'])
    return redirect(f"http://localhost:5173?access_token={token_info['access_token']}&refresh_token={token_info['refresh_token']}")
    # return jsonify(token_info)
    # return "Logged in to Spotify successfully!"


@app.route('/spotify/playlists')
def spotify_playlists():
    token_info = session.get('token_info')

    # Ensure the token info exists and is valid
    if not token_info:
        # return redirect('/spotify/login')
        return jsonify(message="You need to login to spotify!")

    sp = spotipy.Spotify(auth=token_info['access_token'])
    playlists = sp.current_user_playlists()
    return jsonify(playlists)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
