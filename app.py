from flask import Flask
from flask import request

# Third-party imports
from ytmusicapi import YTMusic

ytmusic = YTMusic("oauth.json")
app = Flask(__name__)

@app.get("/v1/playlists")
def getPlaylists():
    return ytmusic.get_library_playlists()

@app.post("/v1/playlists")
def createPlaylist():
    request_data = request.get_json()

    title = request_data['title']
    description = request_data.get('description', '')
    privacy_status = request_data.get('privacyStatus', 'PRIVATE')
    video_ids = request_data.get('videoIds', None)
    source_playlist = request_data.get('sourcePlaylist', None)

    return ytmusic.create_playlist(title, description, privacy_status, video_ids, source_playlist)

@app.get("/v1/playlists/<playlist_id>")
def getPlaylist(playlist_id):
    return ytmusic.get_playlist(playlist_id)

@app.post("/v1/playlists/<playlist_id>/add-songs")
def addToPlaylist(playlist_id):
    request_data = request.get_json()

    video_ids = request_data.get('videoIds', None)
    source_playlist = request_data.get('source_playlist', None)
    duplicates = request_data.get('duplicates', False)

    app.logger.debug('%s video ids',video_ids)

    return ytmusic.add_playlist_items(playlist_id, video_ids, source_playlist, duplicates)

@app.get("/v1/users/<channel_id>")
def getUser(channel_id):
    return ytmusic.get_user(channel_id)

@app.get("/v1/search")
def search():
    query_params = request.args

    query = query_params.get('query')
    filter = query_params.get('filter', 'songs')
    scope = query_params.get('scope')
    limit = query_params.get('limit', 20)
    ignore_spelling = query_params.get('ignoreSpelling', False)

    return ytmusic.search(query, filter, scope, limit, ignore_spelling)




