import requests
from bs4 import BeautifulSoup

def intern_meroIntern():
    URL = "https://merointernship.com/category/internship/"
    page = requests.get(URL)

    titles = []
    authors = []
    dates = []

    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find(id="content_box")
    job_elements = results.find_all("article", class_="latestPost excerpt")
    # job_elements = results.find_all("h2", class_="title front-view-title")

    for job_element in job_elements:
        title_element = job_element.find("h2", class_="title")
        titles.append(title_element.text.strip())
        author_element = job_element.find("span", class_="theauthor")
        authors.append(author_element.text.strip())
        date_element = job_element.find("span", class_="thetime date updated")
        dates.append(date_element.text.strip())

        # print(job_element, end="\n"*2)

        # print(title_element.text.strip(), end="\n")
        # print(author_element.text.strip(), end="\n")
        # print(date_element.text.strip(), end="\n"*2)

    
    return titles, authors, dates

intern_meroIntern()