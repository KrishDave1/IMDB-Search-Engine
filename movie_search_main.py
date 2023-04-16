from imdb import IMDb
import pandas as pd
import pyttsx3
from tabulate import tabulate
import questionary

engine = pyttsx3.init()
engine.setProperty('rate', 195)
engine.setProperty('volume', 1.5)


print("\nWelcome to the IMDB movie search engine")
engine.say("Welcome to the IMDB movie search engine")
engine.runAndWait()


engine.say("Please enter the name of the movie you want to search for")
engine.runAndWait()
movie_name = input("\nEnter the name of the movie you want to search for: ")
engine.say("Good choice. Searching for " + movie_name)


ia = IMDb()
name_l = []
search_result = ia.search_movie(movie_name)
for i in search_result:
    name_l.append(i['title'])


engine.say("Here are the search results")
engine.runAndWait()
dict = {"Movie Name":name_l}
df = pd.DataFrame(dict)
print(tabulate(df, headers='keys', tablefmt='psql'))
print("\n")

engine.say("Please enter the serial number of the movie you want to search for")
engine.runAndWait()
serial_no = int(input("Enter the serial number of the movie you want to search for: "))
print("\n")
movie_name = search_result[serial_no]['title']



# searching the name 
search = ia.search_movie(movie_name)
# getting the id
id = search[0].movieID
# printing it
print("You Selected: ",search[0]['title'] + " : " + id )
name = search[0]['title']
print("\n")



# getting the movie
import webbrowser


def generate_movie_info_html(imdb_id):
    ia = IMDb()
    movie = ia.get_movie(imdb_id)
    

    # Get movie information
    movie_info = {
        'Title': movie.get('title'),
        'Year': movie.get('year'),
        'Genre': ', '.join(movie.get('genres', [])),
        'Runtime': movie.get('runtimes')[0],
        'Rating': movie.get('rating'),
        'Votes': movie.get('votes'),
        'Director': ', '.join([d.get('name') for d in movie.get('directors', [])]),
        'Cast': ', '.join([c.get('name') for c in movie.get('cast', [])]),
        'Poster': movie.get('cover url'),
        'Language': ', '.join(movie.get('languages', [])),
        'Country': ', '.join(movie.get('countries', [])),
        'Awards': movie.get('awards'),
        'Release Date': movie.get('original air date'),
        'Tagline': movie.get('tagline'),
        'Gross': movie.get('box office').get('Cumulative Worldwide Gross') if movie.get('box office') else '',
        'Sound Mix': ', '.join(movie.get('sound mix', [])),
        'plot outline': movie.get('plot outline'),
    }

    # Generate HTML file
    with open('movie_info.html', 'w', encoding='utf-8') as file:
        file.write('<html>\n')
        file.write('<head>\n')
        file.write('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">\n')
        file.write('</head>\n')
        file.write('<body>\n')
        file.write('<div class="container mt-5">\n')
        file.write('<h1 class="text-center mb-4">{}</h1>\n'.format(movie_info['Title']))
        file.write('<table class="table table-bordered table-striped table-hover mt-4">\n')
        for key, value in movie_info.items():
            file.write('<tr>\n')
            file.write('<th scope="row" class="text-uppercase">{}</th>\n'.format(key))
            if(key == 'Poster'):
                file.write('<td><img src="{}" alt="Poster" class="img-fluid rounded"></td>\n'.format(value))
            else:
                file.write('<td>{}</td>\n'.format(value))
            file.write('</tr>\n')
        file.write('</table>\n')
        file.write('</div>\n')
        file.write('<script src="https://code.jquery.com/jquery-3.5.1.slim.min.js"></script>\n')
        file.write('<script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.9.1/dist/umd/popper.min.js"></script>\n')
        file.write('<script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>\n')
        file.write('</body>\n')
        file.write('</html>\n')

        # Open HTML file in a web browser
        webbrowser.open('movie_info.html')


# Example usage
imdb_id = id  # IMDb ID for the movie "Inception"
generate_movie_info_html(imdb_id)

import os
from  pyhtml2pdf import converter
path = os.path.abspath('movie_info.html')
converter.convert(f'file:///{path}',f'{name}.pdf')
print("Your file is ready")

