from flask import Flask, render_template
import crawler

app = Flask(__name__)

@app.route("/")
def hello():
    artist = crawler.get_all_artist()
    return render_template("index.html", artists=artist )


@app.route("/songs/<int:id>")
def list_all_songs(id):
    songs = crawler.get_all_songs(id)
    artist = crawler.singer(id)
    artists = crawler.get_all_artist()
    return render_template("songlist.html", artist=artist, songs=songs, artists=artists, current=id)


@app.route("/songs/<int:id>/lyrics/<int:sid>")
def lyrics(sid,id):
    songs = crawler.get_all_songs(id)
    artist = crawler.singer(id)
    artists = crawler.get_all_artist()
    lyrics= crawler.get_lyrics(sid)
    return render_template("lyrics.html", lyrics=lyrics, songs=songs, artists=artists, artist=artist, current=sid)


if __name__ == "__main__":
    app.run(debug=True)