from bs4 import BeautifulSoup

def clean(text):
    cleantext = BeautifulSoup(text,"lxml").text
    return cleantext