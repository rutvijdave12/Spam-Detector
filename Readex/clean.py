#Used to clean the content
from bs4 import BeautifulSoup

def clean(text):
    cleantext = BeautifulSoup(text,"lxml").text
    #lxml is a Python library which allows for easy handling of XML and HTML files, and can also be used for web scraping.
    return cleantext
