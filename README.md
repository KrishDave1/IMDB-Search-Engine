# IMDB SEARCH ENGINE

The IMDb Web Scraping Project provides a Python-based solution to scrape movie data from IMDb. It utilizes web scraping techniques to extract information from IMDb's website and stores it in a structured format for further analysis or integration with other projects. The project includes a set of scripts that allow you to scrape different types of movie data, such as top-rated movies, most popular movies, upcoming movies, and more.

## FEATURES
* Scrapes movie data from IMDb using Python web scraping techniques.
* Extracts movie information, including titles, release dates, genres, ratings, and more.
* Provides customizable options to scrape specific types of movie data.
* Stores scraped data in a structured format for easy analysis and integration with other projects.
* Includes documentation and examples to help you get started quickly.
* Provides graphs to anlayze data easily.

## DESCRIPTION
The application provides the following functionalities:

* Movie search: Users can search for movies by title, genre, or any other relevant criteria. The application uses web scraping with BeautifulSoup to fetch movie data from IMDB's website and displays it to the user.

* Movie details: Users can view detailed information about a particular movie, including its title, genre, release year, ratings, and other relevant information. This information will be available to the user in html as well as pdf format.

* User-friendly GUI: The application has a basic graphical user interface (GUI) built using the Tkinter library, which provides a simple and intuitive way for users to interact with the application.

* Data visualization: The application also provides basic data visualization using Matplotlib, allowing users to view graphical representations of movie ratings and other relevant data.

## GETTING STARTED

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

```
git clone https://github.com/Transyltooniaa/hackathon-scrapping.git
```

## PREREQUISITES
Before you can deploy and use the IMDb web scraper project, please make sure you have the following prerequisites in place:

* Python: The project is implemented in Python and requires Python to be installed on your machine. You can download and install Python from the official Python website (https://www.python.org/).

* Beautiful Soup and Requests libraries: The project relies on the Beautiful Soup and Requests libraries for web scraping. You can install these libraries using pip (see installing section for more details)

* Web browser and web driver: Depending on your use case, you may need a web browser and a web driver. If you plan to scrape data from a web page that requires HTML to load, you may need to use Beautiful Soup. You can download and install the appropriate web driver for your web browser from the official websites, such as ChromeDriver (https://sites.google.com/a/chromium.org/chromedriver/downloads) for Chrome, GeckoDriver (https://github.com/mozilla/geckodriver/releases) for Firefox, or Microsoft Edge WebDriver (https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/) for Microsoft Edge.

* IMDb website access: The project is designed to scrape data from the IMDb website (https://www.imdb.com/). Make sure you have access to the IMDb website and comply with their terms of use, privacy policy, and robots.txt file. Respect their rules and regulations while using their data.

* Basic programming skills: The project requires basic programming skills in Python, including understanding of Python syntax, data structures, and file operations. If you are new to Python, it's recommended to familiarize yourself with Python programming concepts before using the IMDb web scraper project.

* A basic idea of other modules used. Even if you are new to them . It is quite easy to understand them. List of modules can be found below (modules section). For details about any module refer to (https://www.geeksforgeeks.org/)

By ensuring that you have the above prerequisites in place, you will be well-prepared to deploy and use the IMDb web scraper project for your web scraping needs.


### INSTALLATION

A step by step series of examples that tell you how to get a development env running


#### Modules
* bs4
```
pip install bs4 
```
* requests
```
pip install requests
```
* pandas
```
pip install pandas
```
* tabulate 
```
pip install tabulate
```
* matplotlib
```
pip install matplotlib
```
* numpy
```
pip install numpy
```
* seaborn
```
pip install seaborn
```
* pyttsx3
```
pip install pyttsx3
```
* imdb
```
pip install IMDbPY
```
* pretty_html_table
```
pip install pretty-html-table
```
* questionary
``` 
pip install questionary
```

## EXECUTION
Enter the command wriiten below to execute the program on command line terminal
``` 
python3 faster_main.py
```

## BUILT WITH

* Python: The project is primarily built using Python programming language, which provides powerful tools and libraries for web scraping.
* Beautiful Soup: A popular Python library for web scraping that makes it easy to extract data from HTML and XML documents.
* Requests: A Python library for making HTTP requests to web servers, which is commonly used in combination with Beautiful Soup to fetch web pages for scraping.
* HTML and XML: The project relies on HTML and XML markup languages, which are standard markup languages for creating web pages and exchanging data on the web.
* IDE or Text Editor: The project may be developed using an Integrated Development Environment (IDE) like PyCharm, VSCode, or Sublime Text, or a text editor like Notepad++ or Atom, depending on the developer's preference.
* Git: A widely used version control system for tracking changes in the project's source code and collaborating with other developers.
* GitHub: A popular web-based hosting service for Git repositories, used for storing and sharing the project's source code.
* Command Line: The project may be run and managed using the command line interface (CLI), which is a text-based interface for interacting with the project's code and running scripts.

## CONTRIBUTING

We welcome contributions to the Beautiful Soup project! If you have any suggestions, bug reports, or feature requests, please open an issue on GitHub or submit a pull request. We appreciate your feedback and collaboration in making this project even better!

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## VERSIONING

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## AUTHORS

* **Krish Dave** - *co-founder* - [KrishDave1](https://github.com/KrishDave1)
* **Ajitesh Kumar Singh** - *co-founder* - [Transyltooniaa](https://github.com/Transyltooniaa)



See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## LICENSE

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## ACKNOWLEDGEMENTS
* GeeksForGeeks
* Stack Overflow
* ChatGPT
* Abhinav Kumar
* Seniors
