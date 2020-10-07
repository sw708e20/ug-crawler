import requests
from bs4 import BeautifulSoup

for i in range(151):
    r = requests.get(f"https://www.ug.dk/alfabetisk/uddannelser?page={i}")
    bs = BeautifulSoup(r.text, 'html.parser')
    lst = bs.find_all("div", "views-row")
    for edu in lst:
        print(edu.find("h2").string)
        print(edu.find("a")["href"])
        edu_lst = edu.find_all("div", "field-item even")
        print(edu_lst[0].string)
        print(edu_lst[1].string)
