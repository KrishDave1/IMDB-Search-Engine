from imdb import IMDb
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np

# Initialize IMDb module
ia = IMDb()

# Prompt user for movie name
movie_name = input("Enter the name of the movie you want to search for: ")

# Search for movies with the given name
search_result = ia.search_movie(movie_name)

# Display search results
print("Search results:")
for i, movie in enumerate(search_result):
    print(f"{i+1}. {movie['title']}")

# Prompt user to select a movie
serial_no = int(
    input("Enter the serial number of the movie you want to search for: "))
selected_movie = search_result[serial_no - 1]

# Retrieve IMDb ID of the selected movie
imdb_id = selected_movie.movieID

# Get detailed movie information
movie = ia.get_movie(imdb_id)

# Extract movie details for feature vector
title = movie.get('title', '')
year = str(movie.get('year', ''))
genre = ', '.join(movie.get('genres', []))
runtime = str(movie.get('runtimes', [''])[0])
rating = str(movie.get('rating', ''))
votes = str(movie.get('votes', ''))
director = ', '.join([d.get('name', '') for d in movie.get('directors', [])])
cast = ', '.join([c.get('name', '') for c in movie.get('cast', [])])
language = ', '.join(movie.get('languages', []))
country = ', '.join(movie.get('countries', []))
awards = movie.get('awards', '')
release_date = movie.get('original air date', '')
tagline = movie.get('tagline', '')
gross = movie.get('box office', {}).get('Cumulative Worldwide Gross', '')
sound_mix = ', '.join(movie.get('sound mix', []))
plot_outline = movie.get('plot outline', '')

# Concatenate movie details into a single string
movie_details = ' '.join([title, year, genre, runtime, rating, votes, director, cast,
                         language, country, awards, release_date, tagline, gross, sound_mix, plot_outline])

# Create feature vector using TfidfVectorizer
vectorizer = TfidfVectorizer()
feature_vector = vectorizer.fit_transform([movie_details])

# Convert feature vector to a numpy array
feature_vector = feature_vector.toarray()

# Print feature vector
print("Feature vector:")
print(feature_vector)

exist = np.load('movie.npy')
new = np.concatenate((exist, feature_vector[:100]), axis=0)
print(new)
# try:
#     np.save('movie.npy', new)
#     print("ADDED")
# except:
#     np.save('movie.npy', feature_vector)
#     print("DONE")
