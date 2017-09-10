'''
Image Scraper
J.G.

needs BeautifulSoup4 installed

1. change TARGET_URL to download a set of images that are each located with 
    href tags in a web page
2. change DIRNAME to the name that you want for your folder, where the images
    will be downloaded to. By default, this folder will be created if not extant
3. change the bsObj.findAll criteria according to the html structure that you are
    trying to download from
    You may need to add separate code if you want to download a set of items
    that do not have the html tag scheme as one another
    
Run from the console:
$ python img-scraper.py
'''

from urllib.request import urlopen, urlretrieve
from urllib.error import HTTPError
from bs4 import BeautifulSoup as bsp
import os
import time

def dirmaker(dirname):
    if not os.path.exists(dirname):
        try:
            os.makedirs(dirname)
            print("%s was created" % dirname)
        except Exception as e:
            print(e)
            print("%s could not be created or already exists")


def scraper(url,dirname):
    try:
        html = urlopen(url)
        bsObj = bsp(html)
        images = bsObj.findAll("a", {"rel":"lightbox"})
        
        dirmaker(dirname)
        
        for i in images:
            u = i['href']
            fname = dirname + "/" + u.split("/")[-1]
            urlretrieve(u, fname)
        
    except HTTPError as e:
        print(e)
    finally:
        print("**********************************")


if __name__ == '__main__':
    start = time.time()
    TARGET_URL = "http://pokemonprices.com/set/Gym+Heroes"
    DIRNAME = "gymHeroes"
    scraper(TARGET_URL, DIRNAME)
    end = time.time()
    t = end - start
    print("Scraping completed in %s seconds" % str(int(t)) )
    
    