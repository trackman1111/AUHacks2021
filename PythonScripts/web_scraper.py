import requests
from bs4 import BeautifulSoup

sectionDivs = []
states = []
info = []
Orders = []

URL = 'https://www.aarp.org/health/healthy-living/info-2020/states-mask-mandates-coronavirus/'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html5lib')
overDiv = soup.find_all("div", {"class": "everywhere-article-content parsys"})

for div in overDiv:
    sectionDivs += div.find_all("div", {"class": "aarpe-text-image"})

for subsec in sectionDivs:
    for header in subsec.find_all("h4"):
        states.append(header.text.rstrip("\n").rstrip("\xa0"))
    for p in subsec.find_all("p"):
        if "Statewide order" in p.text:
            info += p

for i in range(0,len(info),2):
    print(info[i].text + info[i+1])

del states[-1]

print(Orders)
