import requests
from bs4 import BeautifulSoup
import time
import webbrowser
from datetime import datetime

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
        # section = response.find('p', class_='select-color-1')
        section = response.find('p', { 'data-altcopy' : 'product_coming_soon_1'})
        if section is None:
            linkChanged = True
        else:
            print(section)
            print(datetime.now().time())
    open_url(link)

if __name__ == '__main__':main()