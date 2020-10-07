import requests
from bs4 import BeautifulSoup

for i in range(151):
    r = requests.get(f"https://www.ug.dk/alfabetisk/uddannelser?page={i}")
    bs = BeautifulSoup(r.text, 'html.parser')
    titles = bs.find_all("h2")
    for edu in titles:
        if edu.string is not None:
            print(edu.string)
