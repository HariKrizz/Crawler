from flask import Flask, render_template
import crawler

app = Flask(__name__)

@app.route("/")
def hello():
    artist = crawler.get_all_artist()
    return render_template("index.html", artists=artist )
    # return "<h1>Hello World</h1>"


@app.route("/lyrics/<int:id>")
def list_all_songs(id):
    songs = crawler.get_all_songs(id)
    artist= crawler.singer(id)
    return render_template("songlist.html", artist=artist[0],songs=songs)


@app.route("/lyric/<int:sid>")
def lyrics(sid):
    lyrics= crawler.get_lyrics(sid)
    return render_template("lyrics.html", lyrics=lyrics)

if __name__ == "__main__":
    app.run(debug=True)