import imdb
import pandas as pd
from tabulate import tabulate
import pyttsx3
import questionary

engine = pyttsx3.init()
engine.setProperty('rate', 195)
engine.setProperty('volume', 1.5)


class IMDbMovieSearchEngine:
    def __init__(self):
        self.genres = ["comedy", "sci-fi", "horror", "romance", "action", "thriller", "drama", "mystery",
                    "crime", "animation", "adventure", "fasntasy", "comedy-romance", "action-comedy", "superhero"]
        self.sort_by = {"popularity": "popularity", "a-z": "alpha", "user rating": "user_rating", "number of votes": "num_votes",
                        "us box office": "boxoffice_gross_us", "runtime": "runtime", "year": "year", "release date": "release_date"}
        self.sort = ["popularity", "A-Z", "User Rating", "Number of Votes",
                    "US Box Office", "Runtime", "Year", "Release date"]
        self.url = None

    def display_genres(self):
        dict_genre = {"Type of genre": self.genres}
        df_genre = pd.DataFrame(dict_genre)
        print("\n\nHere are the genres:")
        engine.say("Here are the genres to choose from")
        engine.runAndWait()
        print(tabulate(df_genre, headers='keys', tablefmt='psql'))

    def display_sort_options(self):
        dict_sort = {"Sort by": self.sort}
        df_sort = pd.DataFrame(dict_sort)
        print("\nHere are the sort options")
        engine.say("Here are the sort options")
        engine.runAndWait()
        print(tabulate(df_sort, headers='keys', tablefmt='psql'))

    def get_genre_inputs(self):
        engine.say("Please enter the genre you want to search for")
        engine.runAndWait()
        genres = input("\nEnter the genre you want to search for (write the name): ")
        self.genres = genres.lower()
    def get_sort_inputs(self):
        engine.say("Please enter the sort order you want to search for")
        engine.runAndWait()
        sort_inp = input("\nEnter the sort order you want to search for (enter the name): ")
        self.sort_inp = sort_inp.lower()
        engine.say("Please enter the sorting order you want to search for (asscending or descending)")
        engine.runAndWait()
        
        order = questionary.select(
        "\nDo you want to see the detail in ascending or descending order?",
        choices=["asc", "desc"]
            ).ask()
        
        self.order = order.lower()

    def generate_url(self):
        self.url = f"https://www.imdb.com/search/title/?genres={self.genres}&view=simple&sort={self.sort_by[self.sort_inp]},{self.order}"



# Create an instance of the IMDbMovieSearchEngine class
imdb_search_engine = IMDbMovieSearchEngine()

# Display available genres and sort options
imdb_search_engine.display_genres()

# Get user inputs for genre, sort order, and sorting order
imdb_search_engine.get_genre_inputs()

# Display available genres and sort options
imdb_search_engine.display_sort_options()

# Get user inputs for genre, sort order, and sorting order
imdb_search_engine.get_sort_inputs()

# Generate the URL for movie search
imdb_search_engine.generate_url()
genre_url=imdb_search_engine.url
