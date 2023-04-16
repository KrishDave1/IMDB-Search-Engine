import requests
from bs4 import BeautifulSoup
import pandas as pd
from tabulate import tabulate
import pyttsx3

# Initialize the text-to-speech engine
engine = pyttsx3.init()
engine.setProperty('rate', 195)
engine.setProperty('volume', 1.5)

topics_url = 'https://www.imdb.com/chart/boxoffice/'
response = requests.get(topics_url)
if response.status_code != 200:
    raise Exception(f"Failed to load page {response}")
# else:
    # print("Page loaded successfully")

page_contents = response.text
# print(page_contents[:1000])

soup = BeautifulSoup(page_contents, 'html.parser')


def extractor(classes, tag):
    l = []
    selection_class = classes
    topic_title_tags = soup.find_all(tag, {'class': selection_class})
    for i in topic_title_tags:
        tmp = i.text.strip()
        if tmp == "":
            l.append("N/A")
        else:
            l.append(tmp)

    return l


def title_column():
    title_l = extractor("titleColumn", "td")
    movie_name = []
    for i in title_l:
        l = i.split("\n")
        n1 = l[0].rstrip()
        movie_name.append(n1)
    return movie_name
# print(title_column())


def Weekend_column():
    l = []
    selection_class = 'ratingColumn'
    topic_title_tags = soup.find_all('td', {'class': selection_class})
    j = 0
    for i in topic_title_tags:
        new = i.text.strip()
        if j % 2 == 0:
            l.append(new)
        j += 1
    return l


def Gross_column():
    gross_l = extractor("secondaryInfo", "span")
    return gross_l


def link():
    base_link = "https://www.imdb.com"
    selection_class = "titleColumn"
    topic_title_tags = soup.find_all("td", {'class': selection_class})
    link_l = []
    for i in topic_title_tags:
        link = i.find('a')['href']
        link_l.append(base_link + link)
    return link_l


def weeks_column():
    weeks_l = extractor("weeksColumn", "td")
    return weeks_l


dict = {'Movie Name': title_column(),
        'Weekend': Weekend_column(),
        'Gross': Gross_column(),
        'Weeks': weeks_column(),
        'Link': link()
        }
df = pd.DataFrame(dict)
engine.say("Here are the top 10 movies of the week")
engine.runAndWait()
print(tabulate(df, headers='keys', tablefmt='psql'))
