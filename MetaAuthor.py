import requests
from bs4 import BeautifulSoup as soup
import urlparse

def scraping():
    url = raw_input("Enter a valid url link: ")
    if urlparse.urlsplit(url)[0] != "http" or urlparse.urlsplit(url)[0] != "https":
        url = "http://" + url
    get = requests.get(url)
    read = soup(get.text)
    return read.select("meta")

def choice():
    choice_input = raw_input("Enter Author to get Author Description or All to get all Meta Description :")
    if choice_input == "All" or choice_input == "all":
        print scraping()
    else:
        print scraping(), "Author"

choice()

