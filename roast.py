import random
import requests
from bs4 import BeautifulSoup

def roast_me():
    URL="https://bestlifeonline.com/yo-mama-jokes/"
    page = requests.get(URL)

    jokes = []

    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find("div", class_="content noskimwords")
    lists = results.find_all("ol")
    for each in lists:
        joke_val = each.find("li")
        jokes.append(joke_val.text.strip())
    
    return random.choice(jokes)

# print(roast_me())