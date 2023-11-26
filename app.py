from flask import Flask
from ytmusicapi import YTMusic

ytmusic = YTMusic("oauth.json")
app = Flask(__name__)

@app.get("/v1/playlists")
def getPlaylists():
    return ytmusic.get_library_playlists()