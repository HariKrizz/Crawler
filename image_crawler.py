import wget
import requests
from bs4 import BeautifulSoup 

heads = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
}


def get_image(image_url):
    image = []
    resp = requests.get(url=image_url, headers=heads)
    soup = BeautifulSoup(resp.content, features="html.parser")
    image_div = soup.find("div", {"class":"GalleryItems-module__searchContent___DbMmK"})

    image_link = image_div.find_all("a")
    for i in image_link:
        image.append(i["href"])
    return image


def image_download(image_url):
    resp = requests.get(url=image_url,headers=heads)
    soup = BeautifulSoup(resp.content, features="html.parser")
    image_div = soup.find("img",{"class":"AssetCard-module__image___dams4"})
    image_link = image_div['src']
    return image_link


def main():
    link = get_image("https://www.gettyimages.in/photos/aamir-khan-actor")
    for i in link:
        wget.download(image_download("https://www.gettyimages.in"+i))


if __name__ == "__main__":
    main()
