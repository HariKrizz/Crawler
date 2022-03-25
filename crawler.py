import os
import requests
import psycopg2
from bs4 import BeautifulSoup

conn = psycopg2.connect(dbname="music", host="localhost", port=5432, user="hari")

def get_artists(url):
    ret=[]
    r = requests.get(url)
    body = r.content
    soup = BeautifulSoup(body, features="html.parser")
    tracklists = soup.find("table", {"class" : "tracklist"})
    links= tracklists.find_all("a")
    for i in links:
        ret.append((i.text,i['href']))
    return ret

def get_songs(artist_url):
    songs=[]
    r = requests.get(artist_url)
    body = r.content
    soup = BeautifulSoup(body, features="html.parser")
    tracklists = soup.find("table", {"class" : "tracklist"})
    links=tracklists.find_all("a")
    for i in links:
        songs.append((i.text,i['href']))
    return songs

def get_lyrics(song_url):
    r = requests.get(song_url)
    body = r.content
    soup = BeautifulSoup(body, features="html.parser")
    lyrics_div = soup.find("p", {"id": "songLyricsDiv"})
    lyrics = lyrics_div.text
    return lyrics

def crawl():

    connection = psycopg2.connect("dbname=lyrics")
    cur = connection.cursor()
    
    artists= get_artists("https://www.songlyrics.com/a/")
    for name, link in artists[:10]:
        cur.execute("INSERT INTO artist (name) VALUES (%s);", (name,))
        songs = get_songs(link)

        for song, song_link in songs:
            print("Song Name: ",song)
            print('-+-+-+-+-+-+-+-+-+-+-+-+-')
            lyrics = get_lyrics(song_link) 
            cur.execute("INSERT INTO song (artist,songname,lyrics) VALUES((select id from artist where name=%s),%s,%s);",(name,song,lyrics)) 
    connection.commit()
    print('Added songs to Database')

        
if __name__ == "__main__":
    crawl()