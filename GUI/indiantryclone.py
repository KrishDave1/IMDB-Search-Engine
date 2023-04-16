import requests
from bs4 import BeautifulSoup
import pandas as pd
import tkinter as tk
from tkinter import ttk


def extractor(classes, tag, soup):
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


def get_data(choice, choice1, choice2, soup):
    base_url = "https://www.imdb.com/india"
    if choice == "1":
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
            title_l = extractor("trending-list-rank-item", "div", soup)
            return title_l
        movie_name = []
        topsearch = []
        for i in title_column():
            new = i.split("\n")
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
        dict = {"Movie Name": movie_name,
                "Top Search": topsearch, "Link": link()}
        df = pd.DataFrame(dict)
        try:
            # Clear existing data
            df_tree.delete(*df_tree.get_children())

            # Retrieve data from the API
            response = requests.get(url)
            data = response.json()

            # Iterate through the data and insert into the Treeview
            for index, row in enumerate(data, start=1):
                df_tree.insert("", tk.END, text=index, values=(
                    row["Rank"], row["Movie Name"], row["Year"], row["Rating"], row["Link"]))

        except Exception as e:
            print("Error: ", e)

    elif choice == "2":
        if choice1 == "1":
            edit_url = '/top-rated-indian-movies/'
            text = "Indian"
        elif choice1 == "2":
            edit_url = '/top-rated-tamil-movies/'
            text = "Tamil"
        elif choice1 == "3":
            edit_url = '/top-rated-telugu-movies/'
            text = "Telugu"
        elif choice1 == "4":
            edit_url = '/top-rated-malayalam-movies/'
            text = "Malayalam"
        print(f"How do you want to sort Top {text} Movies of All Time")
        print("1.By Rating")
        print("2.By Release Date")
        print("3.By Popularity(Number of Votes)")
        if choice2 == "2":
            edit_url = edit_url+"?sort=us,desc&mode=simple&page=1"
        elif choice2 == "3":
            edit_url = edit_url+"?sort=nv,desc&mode=simple&page=1"
        topics_url = base_url + edit_url
    response = requests.get(topics_url)
    page_contents = response.text
    soup = BeautifulSoup(page_contents, 'html.parser')

    def title_column():
        title_l = extractor("titleColumn", "td")
        return title_l
    number = []
    movie_name = []
    year = []
    for i in title_column():
        new = i.split("\n")
        number.append(new[0])
        n1 = new[1].lstrip()
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
    dict = {
        "Number Acc to Rating": number,
        "Movie Name": movie_name,
        "Year": year,
        "Rating": rating_column(), "Link": link()
    }
    df = pd.DataFrame(dict)


def on_item_selected(event):
    selected_item = df_tree.selection()[0]
    item = df_tree.item(selected_item)
    print("Selected Item: ", item)


def on_refresh():
    get_data()


def show_details(event):
    item_id = df_tree.focus()
    item = df_tree.item(item_id)
    movie_name = item["values"][0]
    webbrowser.open_new_tab(movie_name)


def on_close():
    root.destroy()


# Create tkinter window
root = tk.Tk()
root.title("IMDb Movie Scraper")

# Create frames
frame1 = ttk.Frame(root)
frame1.pack(side=tk.TOP, padx=10, pady=10, fill=tk.X)

frame2 = ttk.Frame(root)
frame2.pack(side=tk.TOP, padx=10, pady=10, fill=tk.BOTH, expand=True)

# Create labels
label1 = ttk.Label(frame1, text="Select an option:")
label1.pack(side=tk.LEFT, padx=5)

# Create comboboxes
options1 = ["1. Most Anticipated New Indian Movies and TV Shows", "2. Top Rated Indian Movies",
            "3. Top Rated Tamil Movies", "4. Top Rated Telugu Movies", "5. Top Rated Malayalam Movies"]
combo1 = ttk.Combobox(frame1, values=options1, width=50)
combo1.pack(side=tk.LEFT, padx=5)

options2 = ["1. Sort by Rating", "2. Sort by Release Date",
            "3. Sort by Popularity (Number of Votes)"]
combo2 = ttk.Combobox(frame1, values=options2, width=30)
combo2.pack(side=tk.LEFT, padx=5)

options3 = ["1. Ascending", "2. Descending"]
combo3 = ttk.Combobox(frame1, values=options3, width=20)
combo3.pack(side=tk.LEFT, padx=5)

options4 = ["1. Default", "2. IMDb", "3. Tomato Meter",
            "4. Box Office", "5. Runtime", "6. Year"]
combo4 = ttk.Combobox(frame1, values=options4, width=20)
combo4.pack(side=tk.LEFT, padx=5)

# Create buttons
button1 = ttk.Button(frame1, text="Get Data", command=lambda: get_data(
    combo1.get()[0], combo1.get()[3:], combo2.get()[0], combo3.get()[0]))
button1.pack(side=tk.LEFT, padx=5)

button2 = ttk.Button(frame1, text="Clear",
                     command=lambda: df_tree.delete(*df_tree.get_children()))
button2.pack(side=tk.LEFT, padx=5)

button3 = ttk.Button(frame1, text="Exit", command=on_close)
button3.pack(side=tk.RIGHT, padx=5)

# Create treeview
df_tree = ttk.Treeview(frame2)
df_tree.pack(side=tk.LEFT, padx=10, pady=10, fill=tk.BOTH, expand=True)
df_tree.heading("#0", text="Index", anchor=tk.CENTER)
df_tree.column("#0", width=50, anchor=tk.CENTER)
df_tree.heading("#1", text="Rank", anchor=tk.CENTER)
df_tree.column("#1", width=50, anchor=tk.CENTER)
df_tree.heading("#2", text="Movie Name", anchor=tk.CENTER)
df_tree.column("#2", width=200, anchor=tk.CENTER)
df_tree.heading("#3", text="Year", anchor=tk.CENTER)
df_tree.column("#3", width=100, anchor=tk.CENTER)
df_tree.heading("#4", text="Rating", anchor=tk.CENTER)
df_tree.column("#4", width=100, anchor=tk.CENTER)
df_tree.heading("#5", text="Link", anchor=tk.CENTER)
df_tree.column("#5", width=300, anchor=tk.CENTER)

# Bind selection event
df_tree.bind("<<TreeviewSelect>>", on_item_selected)

# Run tkinter event loop
root.mainloop()
