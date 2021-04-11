import requests
from bs4 import BeautifulSoup
import html5lib


def food_scrape():
    states = []
    status = []

    URL = 'https://blog.opentable.com/2021/states-provinces-restaurants-reopen-guide-coronavirus/'
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, 'html5lib')
    main_div = soup.find_all("div", {"class": "entry-content"})

    for i in main_div[0].find_all("h3"):
        states.append(i.text)

    for i in main_div[0].find_all("p"):
        if "Restaurants status:" in i.text:
            status.append(i.text)

    return dict(zip(states,status))