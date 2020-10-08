import requests
from bs4 import BeautifulSoup
import json


class Education:
    def __init__(self, name, link, edu_type, description):
        self.name = name
        self.link = link
        self.edu_type = edu_type
        self.description = description


f = open("educations.json", "a")
for i in range(151):
    r = requests.get(f"https://www.ug.dk/alfabetisk/uddannelser?page={i}")
    bs = BeautifulSoup(r.text, 'html.parser')
    lst = bs.find_all("div", "views-row")
    for edu in lst:
        name = edu.find("h2").string
        link = "https://www.ug.dk" + edu.find("a")["href"]
        edu_lst = edu.find_all("div", "field-item even")
        edu_type = edu_lst[0].string
        description = edu_lst[1].string
        description = description.replace("\r\n", "")
        e = Education(name, link, edu_type, description)
        json_str = json.dumps(e.__dict__, ensure_ascii=False)
        f.write(json_str)
        f.write("\n")
    print(i)
f.close()


