import requests
from bs4 import BeautifulSoup
import time
import webbrowser

def make_request(link):
    request = requests.get(link, timeout=2)
    time.sleep(8)
    return request

def open_url(link):
    webbrowser.open(link, new=2)

def main():
    link = 'http://www.adidas.com/yeezy'
    linkChanged = False
    while linkChanged is False:
        request = make_request(link)
        response = BeautifulSoup(request.content, 'html.parser')
        section = response.find('p', class_='select-color-1')
        # section = response.find('p', { 'data-altcopy' : 'product_coming_soon_1'})
        if section is not None:
            linkChanged = True
    open_url(link)

if __name__ == '__main__':main()