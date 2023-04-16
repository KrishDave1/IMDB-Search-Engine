import requests
from bs4 import BeautifulSoup
import pandas as pd
from tabulate import tabulate

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
base_url="https://www.imdb.com/india"
print("Welcome to Indian Database on IMDB")
print("Choose from the following options:")
print("1. Trending Movies")
print("2. Top 250 Indian Movies of All Time")
choice = input("Enter your choice: ")
if choice == "1":
    print("What do you want to see in Trending Page?")
    print("1.Most Anticipated New Indian Movies and TV Shows")
    print("2.Trending Tamil Movies")
    print("3.Trending Telugu Movies")
    choice1=input("Enter your choice: ")
    if choice1 == "1":
        print("Most Anticipated New Indian Movies and TV Shows")
        topics_url = base_url + '/upcoming/'
    elif choice1 == "2":
        print("Showing Trending Tamil Movies")
        topics_url = base_url + '/tamil/'
    elif choice1 == "3":
        print("Showing Trending Telugu Movies")
        topics_url = base_url + '/telugu/'
    response = requests.get(topics_url)
    page_contents = response.text
    soup = BeautifulSoup(page_contents, 'html.parser')
    def title_column():
        title_l = extractor("trending-list-rank-item", "div")
        return title_l
    movie_name=[]
    topsearch=[]
    for i in title_column():
        new=i.split("\n")
        movie_name.append(new[2])
        topsearch.append(new[3])
    def link():
        selection_class = "trending-list-rank-item"
        topic_title_tags = soup.find_all("div", {'class': selection_class})
        l = []
        for i in topic_title_tags:
            tmp = i.find("a")
            l.append(base_url + tmp.get('href'))
        return l
    dict={"Movie Name":movie_name,"Top Search":topsearch,"Link":link()}
    df=pd.DataFrame(dict)
    print(tabulate(df, headers='keys', tablefmt='psql'))
    print("Thank You for using the IMDB Scraper!")
elif choice == "2":
    print("Welcome to the Top 250 Indian Movies of All Time")
    print("What do you want to see in Top 250 Indian Movies of All Time Page?")
    print("1.Top 250 Indian Movies of All Time")
    print("2.Top 250 Tamil Movies of All Time")
    print("3.Top 250 Telugu Movies of All Time")
    print("4.Top 250 Malayalam Movies of All Time")
    choice1=input("Enter your choice: ")
    if choice1 == "1":
        edit_url='/top-rated-indian-movies/'
        text="Indian"
    elif choice1 == "2":
        edit_url='/top-rated-tamil-movies/'
        text="Tamil"
    elif choice1 == "3":
        edit_url='/top-rated-telugu-movies/'
        text="Telugu"
    elif choice1 == "4":
        edit_url='/top-rated-malayalam-movies/'
        text="Malayalam"
    print(f"How do you want to sort Top {text} Movies of All Time")
    print("1.By Rating")
    print("2.By Release Date")
    print("3.By Popularity(Number of Votes)")
    choice2=input("Enter your choice: ")
    if choice2 == "2":
        edit_url=edit_url+"?sort=us,desc&mode=simple&page=1"
    elif choice2 == "3":
        edit_url=edit_url+'?sort=nv,desc&mode=simple&page=1'
    topics_url = base_url + edit_url
    response = requests.get(topics_url)
    page_contents = response.text
    soup = BeautifulSoup(page_contents, 'html.parser')
    def title_column():
        title_l = extractor("titleColumn", "td")
        return title_l
    number=[]
    movie_name=[]
    year=[]
    rating=[]
    for i in title_column():
        new=i.split("\n")
        number.append(new[0])
        n1=new[1].lstrip()
        movie_name.append(n1)
        year.append(new[2])
    def rating_column():
        rating_l = extractor("ratingColumn imdbRating", "td")
        return rating_l
    def link():
        selection_class = "titleColumn"
        topic_title_tags = soup.find_all("td", {'class': selection_class})
        link_l = []
        for i in topic_title_tags:
            link = i.find('a')['href']
            link_l.append(base_url + link)
        return link_l
    dict={
        "Number Acc to Rating":number,
        "Movie Name":movie_name,
        "Year":year,
        "Rating":rating_column()
        ,"Link":link()
    }
    df=pd.DataFrame(dict)
    choice4=input("How many movies do you want to see? ")
    df1=df.head(int(choice4))
    print(tabulate(df1, headers='keys', tablefmt='psql'))
    print("Thank You for using the IMDB Scraper!")









