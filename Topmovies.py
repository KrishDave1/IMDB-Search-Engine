import requests
from bs4 import BeautifulSoup
import pandas as pd
from tabulate import tabulate
import pyttsx3
import questionary

engine = pyttsx3.init()
engine.setProperty('rate', 195)
engine.setProperty('volume', 1.5)



engine.say("How would you like to sort the list by:")
engine.runAndWait()

choice = questionary.select(
        "How would you like to sort the list by:",
        choices=["1. By IMDB Rating", "2. By Release Date","3. By Number of Votes"]
    ).ask()



if choice == "1. By IMDB Rating":
    edit_url = "?sort=ir,desc&mode=simple&page=1"
elif choice == "2. By Release Date":
    edit_url = "?sort=us,desc&mode=simple&page=1"
elif choice == "3. By Number of Votes":
    edit_url = "?sort=nv,desc&mode=simple&page=1"
    
# Get the HTML from the URL

url = "https://www.imdb.com/chart/top/"+ edit_url

response = requests.get(url)

# Get the HTML from the URL
html = response.content

# Parse the HTML
soup = BeautifulSoup(html, "html5lib")

# Extract the data
def extractor(classes, tag):
    l = []
    selection_class = classes
    topic_title_tags = soup.find_all(tag, {'class': selection_class})
    for i in topic_title_tags:
        tmp = i.text.strip()
        l.append(tmp)

    return l


def title_column():
    title_l = extractor("titleColumn", "td")
    new_l = []
    for i in title_l:
        l = i.split("\n")
        new = l[0].rstrip() + l[1].lstrip()
        newer = new.split(".")
        new_l.append(newer[1].lstrip())
    return new_l


def imdb_column():
    imdb_l = extractor("ratingColumn imdbRating", "td")
    return imdb_l


def year_column():
    year_l = extractor("secondaryInfo", "span")
    new_l = []
    for i in year_l:
        l = i.split("(")
        new = l[1].rstrip(")")
        new_l.append(new)
    return new_l


def link():
    base_link = "https://www.imdb.com"
    selection_class = "titleColumn"
    topic_title_tags = soup.find_all("td", {'class': selection_class})
    link_l = []
    for i in topic_title_tags:
        link = i.find('a')['href']
        link_l.append(base_link + link)
    return link_l


dict = {'Title': title_column(), 'Year': year_column(),
        'IMDB Rating': imdb_column(), 'Link': link()}

df = pd.DataFrame(dict)
engine.say("How many movies do you want to see?")
engine.runAndWait()

n = int(input("\nEnter the number of movies you want to see: "))
engine.say("Here are the top " + str(n) + " movies")
engine.runAndWait()
df1=df.head(n)
print(tabulate(df1, headers='keys', tablefmt='psql'))
