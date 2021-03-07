import os
import requests
import random
import threading
from random import randint
from bs4 import BeautifulSoup

GOOGLE_IMAGE = \
    'https://www.google.com/search?site=&tbm=isch&source=hp&biw=1873&bih=990&'

usr_agent = {
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:86.0) Gecko/20100101 Firefox/86.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
    'Accept-Encoding': 'none',
    'Accept-Language': 'en-US,en;q=0.8',
    'Connection': 'keep-alive',
}

SAVED_FOLDER = os.path.join(os.path.dirname(os.path.realpath(__file__)), "images")

#search terms
SEARCH= {"dog": 1, "dogs":2, "pupper":3, "puppers":4, "puppy":5,"doggo":6, "doggie:":7, "cute dogs":8, "small puppies":9, "puppies":10, "doggies":11}

def main():
    if not os.path.exists(SAVED_FOLDER):
        os.mkdir(SAVED_FOLDER)
    clean()
    download_images()
    threading.Timer(300.0, main).start()
    
def clean():
    dir_name = "images/"
    test = os.listdir(dir_name)

    for item in test:
        if item.endswith(".REMOVE_ME"):
            os.remove(os.path.join(dir_name, item))

def download_images():
    data = random.choice(list(SEARCH))
    print(f"searching for {data}")
    num_images = randint(1,80)
    print('searching...')
    
    search_url = GOOGLE_IMAGE + 'q=' + data

    response = requests.get(search_url, headers = usr_agent)
    html = response.text

    soup = BeautifulSoup(html, 'html.parser')
    results = soup.findAll('img', {'class': 'rg_i Q4LuWd'})

    count = 0
    imagelinks= []
    for res in results:
        try:
            link = res['data-src']
            imagelinks.append(link)
            count = count + 1
            if (count >= num_images):
                break
        except KeyError:
            continue

    print(f'Found {len(imagelinks)} images')
    print('downloading...')

    for i, imagelink in enumerate(imagelinks):
        response = requests.get(imagelink)

        imagename = SAVED_FOLDER + '/' + "dog" + str(i+1) + '.jpg'
        with open(imagename, 'wb') as file:
            file.write(response.content)

    print('woof! (done)')

 
if __name__ == '__main__':
    main()
