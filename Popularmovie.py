import requests
from bs4 import BeautifulSoup
import pandas as pd
from tabulate import tabulate
import pyttsx3

# Initialize the text-to-speech engine
engine = pyttsx3.init()
engine.setProperty('rate', 195)
engine.setProperty('volume', 1.5)

topics_url = 'https://www.imdb.com/chart/moviemeter/'
response = requests.get(topics_url)
if response.status_code != 200:
    raise Exception(f"Failed to load page {response}")
# else:
    # print("Page loaded successfully")

page_contents = response.text


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
    new_l = []
    movie_name = []
    year = []
    for i in title_l:
        l = i.split("\n")
        n1 = l[0].rstrip()
        n2 = l[1].lstrip()
        movie_name.append(n1)
        year.append(n2)
        new_l.append(movie_name)
        new_l.append(year)
    return new_l


def imdb_column():
    imdb_l = extractor("ratingColumn imdbRating", "td")
    return imdb_l


def link():
    base_link = "https://www.imdb.com"
    selection_class = "titleColumn"
    topic_title_tags = soup.find_all("td", {'class': selection_class})
    link_l = []
    for i in topic_title_tags:
        link = i.find('a')['href']
        link_l.append(base_link + link)
    return link_l


dict = {'Title': title_column()[0], 'Year': title_column()[
    1], 'IMDB Rating': imdb_column(), 'Link': link()}
df = pd.DataFrame(dict)
engine.say("Here is a list of popular movies on IMDB")
engine.runAndWait()
print(tabulate(df, headers='keys', tablefmt='psql'))
