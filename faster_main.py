import pyttsx3
import time
import pandas as pd
from tabulate import tabulate
import questionary

# Initialize the text-to-speech engine
engine = pyttsx3.init()
engine.setProperty('rate', 195)
engine.setProperty('volume', 1.5)

# Function to display options and get user's choice using questionary.select
def display_options(options):
    choice = questionary.select(
        "Choose an option:",
        choices=options
    ).ask()
    return choice

# Welcome message
print("\nWelcome to the IMDB Scraper!")
engine.say("Welcome to the IMDB Scraper!")
print("Today is a pleasant day to watch movies!\n")
engine.say("Today is a pleasant day to watch movies! Here are some options for you:")
engine.runAndWait()

# Display sorting options
options = [
    "By Genre",
    "List of Top movies of all time",
    "List of Top Box Office movies this weekend",
    "List of Most popular movies of all time",
    "Would you like to go into the Indian movie database?",
    "See your watchlist\n"
]

# Get user's choice
choice = display_options(options)

# Handle user's choice
if choice == 'By Genre':
    import new_sim
elif choice == 'List of Top movies of all time':
    import Topmovies
elif choice == 'List of Top Box Office movies this weekend':
    import Topboxoffice
elif choice == 'List of Most popular movies of all time':
    import Popularmovie
elif choice == 'Would you like to go into the Indian movie database?':
    import Indianmovie
elif choice == 'See your watchlist\n':
    with open('watchlist.txt') as f:
        datafile = f.readlines()
        dict = {"Movie Name": datafile}
        df = pd.DataFrame(dict)
        print(tabulate(df, headers='keys', tablefmt='psql'))
        engine.say("Here is your watchlist")
        print("\nThank you for using the IMDB scraper! ")
        engine.say("Thank you for using the IMDB scraper! Have a nice day! see you soon!")
        engine.runAndWait()
        exit(1)

engine.say("Do you want to see the details for any movie?")
engine.runAndWait()
# Prompt for movie details
b = questionary.select(
    "Do you want to see the details for any movie?",
    choices=["Yes", "No"]
).ask()

time.sleep(1)
if b == 'Yes':
    import movie_search_main
    print("\nDo you want to add the movie in your watchlist?")
    engine.say("Do you want to add the movie in your watchlist?")
    engine.runAndWait()
    c = questionary.select(
        "Choose an option:",
        choices=["Yes", "No"]
    ).ask()
    if c == 'Yes':
        def check():
            with open('watchlist.txt') as f:
                datafile = f.readlines()
            for line in datafile:
                if movie_search_main.name in line:
                    return True
            return False
        fptr = open("watchlist.txt", "a")
        if not check():
            fptr.write(movie_search_main.name + "\n")
        else:
            print("Movie already exists in watchlist")
            engine.say("Movie already exists in watchlist")
            engine.runAndWait()
        fptr.close()

        print("\nThank you for using the IMDB scraper!")
        engine.say("Thank you for using the IMDB scraper!. You can find the details of the movie you searched for in the folder. Have a nice day! see you soon!")
        engine.runAndWait()
        exit(1)

else:
    print("\nThank you for using the IMDB scraper!")
    engine.say("Thank you for using the IMDB scraper! Have a nice day! see you soon! ")
    engine.runAndWait()
    exit(1)

