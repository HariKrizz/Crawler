from flask import Flask
import crawler

app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1>Hello World</h1>"
@app.route("/lyrics")

def list_all_songs(artist="A"):
    songs = crawler.get_all_songs(artist)
    output = []
    output.append(f"<h1>{artist}</h1>")
    output.append("<ol>")
    for i in songs:
        output.append(f"<li>{i[0]}</li>")
    output.append("</ol>")
    return "".join(output)

if __name__ == "__main__":
    app.run(debug=True)