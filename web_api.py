from flask import Blueprint,jsonify
import crawler

api = Blueprint('api', __name__)

@api.route("/artist")
def fetch_Artist():
    artist = crawler.get_all_artist()
    artist_Array = [{'id':i[0],'name':i[1]} for i in artist]
    return jsonify(artist_Array)

@api.route("/songs/<int:id>")
def list_all_songs(id):
    songs = crawler.get_all_songs(id)
    songs_Array = [{'song_id':i[0], 'song_name':i[1]} for i in songs]
    return jsonify(songs_Array)

@api.route("/songs/lyrics/<int:sid>")
def lyrics(sid):
    lyrics= crawler.get_lyrics(sid)
    return jsonify(lyrics)
