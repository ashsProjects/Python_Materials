import requests
from bs4 import BeautifulSoup
import lxml

with open("C:\\Users\\Ayush\\Documents\\Visual Studio Code\\WebDev\\basicJS.html") as html_file:
    soup = BeautifulSoup(html_file, "lxml")

print(soup.prettify())