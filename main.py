import requests
from bs4 import BeautifulSoup

def intern_meroIntern():
    URL = "https://merointernship.com/category/internship/"
    page = requests.get(URL)

    return_val = []

    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find(id="content_box")
    job_elements = results.find_all("article", class_="latestPost excerpt")
    # job_elements = results.find_all("h2", class_="title front-view-title")

    for job_element in job_elements:
        title_element = job_element.find("h2", class_="title")
        author_element = job_element.find("span", class_="theauthor")
        date_element = job_element.find("span", class_="thetime date updated")

        return_val = title_element + '\n' + author_element + '\n' + date_element + '\n'

        # print(job_element, end="\n"*2)

        # print(title_element.text.strip(), end="\n")
        # print(author_element.text.strip(), end="\n")
        # print(date_element.text.strip(), end="\n"*2)

        return return_val
