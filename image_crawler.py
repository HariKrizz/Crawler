import os
import requests
from bs4 import BeautifulSoup
import wget

header = {
    'User-Agent': 'Mozilla/5.0 (MacintoshIntel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
}


def get_image(url):
    image_store = []
    resp = requests.get(url, headers=header)
    soup = BeautifulSoup(resp.content, features="html.parser")
    images = soup.find("div", {"class": "GalleryItems-module__searchContent___DbMmK"})
    link = images.find_all("a")
    for i in link:
       image_store.append((i['href']))
    return image_store


def image_download(url):
    resp = requests.get(url, headers=header)
    soup = BeautifulSoup(resp.content, features="html.parser")
    image_div=soup.find("img",{"class":"AssetCard-module__image___dams4"})
    image_link = image_div['src']
    return image_link


def main(search_query):
    try:
        os.mkdir(search_query)
    except Exception as e:
        print(e)

    image = get_image("https://www.gettyimages.in/photos/"+search_query)
    for i in image:
        pics = wget.download(image_download("https://www.gettyimages.in"+i))
        os.path.join(search_query,pics)

if __name__ == "__main__":
    main("sachin tendulkar")