from bs4 import BeautifulSoup
import requests
import pandas as pd
from tabulate import tabulate
import new
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import time
import pyttsx3
import questionary

# Initialize the text-to-speech engine
engine = pyttsx3.init()
engine.setProperty('rate', 195)
engine.setProperty('volume', 1.5)

# Function to get user's choice
def get_choice(prompt):
    engine.say(prompt)
    engine.runAndWait()
    choice = input(prompt)
    return choice

# Function to display options and get user's choice
def display_options(options):
    for idx, option in enumerate(options, 1):
        print(f"{idx}. {option}")
    choice = get_choice("Enter your choice here: ")
    time.sleep(0.1)
    return choice


class IMDbScraper:
    def __init__(self, url):
        self.url = url
        self.soup = None

    def get_url(self):
        response = requests.get(self.url)
        if response.status_code != 200:
            raise Exception(f"Failed to load page {response}")
        #else:
            #print("\nPage loaded successfully :)\n")
        html = response.content
        self.soup = BeautifulSoup(html, "html5lib")

    def extractor(self, classes, tag):
        l = []
        selection_class = classes
        topic_title_tags = self.soup.find_all(tag, {'class': selection_class})
        for i in topic_title_tags:
            tmp = i.text.strip()
            l.append(tmp)
        return l

    def title_column(self):
        selection_class = "col-title"
        topic_title_tags = self.soup.find_all("div", {'class': selection_class})
        title_l = []
        for i in topic_title_tags:
            title = i.find('a')
            title_l.append(title.text.strip())
        return title_l

    def year_column(self):
        year_l = self.extractor("lister-item-year text-muted unbold", "span")
        return year_l

    def rating_column(self):
        rating_l = self.extractor("col-imdb-rating", "div")
        num_rating_l =[]
        for i in rating_l:
            if i != "-" :
                num_rating_l.append(float(i))
            else:
                num_rating_l.append(0.0)
        
        return num_rating_l

    def movie_link(self):
        base_url = "https://www.imdb.com"
        selection_class = "col-title"
        topic_title_tags = self.soup.find_all("div", {'class': selection_class})
        movie_link_l = []
        for i in topic_title_tags:
            link = i.find('a')
            movie_link_l.append(base_url + link['href'].strip())
        return movie_link_l

    def create_table(self):
        self.get_url()
        dict_table = {"Title": self.title_column(), "Year": self.year_column(), "Rating": self.rating_column(),
                        "Link": self.movie_link()}
        df_table = pd.DataFrame(dict_table)
        f_table = tabulate(df_table, headers='keys', tablefmt='psql')
        return f_table

    def create_graph(self):
        self.get_url()
        dict_graph = {"Title": self.title_column(), "Rating": self.rating_column()}
        df_graph = pd.DataFrame(dict_graph)
        df_graph['Rating'] = df_graph['Rating'].astype(float)
        df_graph = df_graph.sort_values(by='Rating', ascending=False)
        sns.set_style("darkgrid")
        plt.figure(figsize=(10, 10))
        plt.title("Top 50 Movies by Rating")
        plt.xlabel("Rating")
        plt.ylabel("Title")
        plt.xticks(np.arange(0, 50, step=1))
        sns.barplot(x="Rating", y="Title", data=df_graph.head(50))
        plt.draw()
        plt.show()
        plt.close()


# Create an instance of the IMDbScraper class with the desired URL
imdb_scraper = IMDbScraper(new.genre_url)
# Call the create_table method to generate and print the table
print(imdb_scraper.create_table())

engine.say("Do you want to see the details for any movie?")
engine.runAndWait()
b = questionary.select(
    "Do you want to see the details for any movie?",
    choices=["Yes", "No"]
).ask()

time.sleep(1)
if b == 'Yes':
    import movie_search_main
    print("\nDo you want to add the movie in your watchlist?")
    engine.say("Do you want to add the movie in your watchlist?")
    engine.say("Select Yes or No")
    engine.runAndWait()

    c = questionary.select(
    "Do you want to see the details for any movie?",
    choices=["Yes", "No"]
).ask()
    
    
    if c=="Yes":
        def check():
            with open('watchlist.txt') as f:
                datafile = f.readlines()
            for line in datafile:
                if movie_search_main.name in line:
            # found = True # Not necessary
                    return True
            return False  
        fptr=open("watchlist.txt","a")
        if (check()==False):
            fptr.write(movie_search_main.name + "\n")
        else:
            print("Movie already exists in watchlist")
            engine.say("Movie already exists in watchlist")
            engine.runAndWait()
        fptr.close()

    print("\nThank you for using the IMDB scraper!")
    engine.say("Thank you for using the IMDB scraper! You can find a graph of the top 50 movies by rating on a new window in a momen. You can also find the details of the movie you searched for in the folder. Have a nice day! see you soon!")
    engine.runAndWait()
    imdb_scraper.create_graph()
    exit(1)

else:
    print("\nThank you for using the IMDB scraper!")
    engine.say("Thank you for using the IMDB scraper! Have a nice day! see you soon! ")
    engine.runAndWait()
    exit(1)

