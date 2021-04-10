import requests
from bs4 import BeautifulSoup

def main ():
    sectionDivs = []
    states = []
    info = []
    orders = []

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
            if "wide order" in p.text:
                info += p

    del states[-1]
    info.insert(29, info[28].text.replace("Statewide order: ", ""))
    info[28] = info[0]

    for i in range(1,len(info),2):
        orders.append(info[i].replace("\xa0","").replace(" ",""))

    print(states)
    print(orders)

main()
