import requests
import re

class Downloader():
    '''
    Class to retrieve HTML code
    and binary files from a specific website
    '''
    def __init__(self, url):
        self.url = url
        self.contents = ""
        

    def download(self, image_name='', is_image=False):
        browser = requests.get(self.url)
        response = browser.status_code
        if response == 200:
            self.contents = browser.text
        
            
        if is_image:
            image_file = open(image_name, 'wb')
            image_file.write(self.contents)
            image_file.close()

class xkcdParser(Downloader):
    '''
    Class for parsing xkcd.com
    '''
    
    def get_last_comic_number(self):
        try:
            last_comic_number = re.search(r"http://xkcd/(\d+)").group(1)
            last_comic_number = int(last_comic_number)
        except:
            last_comic_number - None
    
