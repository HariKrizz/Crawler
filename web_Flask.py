from flask import Flask, jsonify, render_template
import crawler
import web_api

app = Flask(__name__) 
app.register_blueprint(web_api.api, url_prefix='/api')


@app.route("/")
def base_Page():
    return render_template("base.html")

# @app.route("/artist")
# def fetch_Artist():
#     artist = crawler.get_all_artist()
#     artist_Array = [{'id':i[0],'name':i[1]} for i in artist]
#     return jsonify(artist_Array)


# @app.route("/songs/<int:id>")
# def list_all_songs(id):
#     songs = crawler.get_all_songs(id)
#     songs_Array = [{'song_id':i[0], 'song_name':i[1]} for i in songs]
#     return jsonify(songs_Array)


# @app.route("/songs/lyrics/<int:sid>")
# def lyrics(sid):
#     lyrics= crawler.get_lyrics(sid)
#     return jsonify(lyrics)


if __name__ == "__main__":
    app.run(debug=True)