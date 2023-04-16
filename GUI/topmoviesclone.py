import requests
from bs4 import BeautifulSoup
import pandas as pd
import tkinter as tk
from tkinter import ttk

# Create a tkinter window
root = tk.Tk()
root.title("Movie List")

# Create a Treeview widget
tree = ttk.Treeview(root, columns=(
    "Title", "Year", "IMDB Rating", "Link"), show="headings")

# Add column headings
tree.heading("Title", text="Title")
tree.heading("Year", text="Year")
tree.heading("IMDB Rating", text="IMDB Rating")
tree.heading("Link", text="Link")

# Define a function to populate the table


def populate_table():
    # Clear existing data in the table
    tree.delete(*tree.get_children())

    # Get data from IMDb website
    url = "https://www.imdb.com/chart/top/?sort=ir,desc&mode=simple&page=1"
    response = requests.get(url)
    html = response.content
    soup = BeautifulSoup(html, "html5lib")

    # Extract data from IMDb website
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

    # Sort the table based on selected option
    sort_by = combo_sort.get()
    if sort_by == "Title":
        df.sort_values("Title", inplace=True)
    elif sort_by == "Year":
        df.sort_values("Year", inplace=True, ascending=False)
    elif sort_by == "IMDB Rating":
        df.sort_values("IMDB Rating", inplace=True, ascending=False)

    # Get number of rows to display
    num_rows = combo_rows.get()
    if num_rows != "All":
        num_rows = int(num_rows)
        df = df.head(num_rows)

    # Insert data into the table
    for row in df.itertuples(index=False):
        tree.insert("", "end", values=row)


# Create a button to populate the table
btn_display = ttk.Button(root, text="Display", command=populate_table)
btn_display.pack()

# Create a combo box forthe number of rows to display
combo_rows = ttk.Combobox(
    root, values=["All", "10", "20", "30", "40", "50", "60", "70", "80", "90", "100"])
combo_rows.set("All")
combo_rows.pack()

# Create a combo box for sorting options
combo_sort = ttk.Combobox(root, values=["Title", "Year", "IMDB Rating"])
combo_sort.set("Title")
combo_sort.pack()

# Create a function to update the table when sorting option is changed


def update_table_sort(*args):
    populate_table()

# Create a function to update the table when number of rows to display is changed


def update_table_rows(*args):
    populate_table()


# Bind events to the combo boxes to update the table
combo_rows.bind("<<ComboboxSelected>>", update_table_rows)
combo_sort.bind("<<ComboboxSelected>>", update_table_sort)

# Create a scrollbar for the table
scrollbar = ttk.Scrollbar(root, orient="vertical", command=tree.yview)
scrollbar.pack(side="right", fill="y")
tree.configure(yscrollcommand=scrollbar.set)

# Pack the treeview widget
tree.pack(expand="yes", fill="both")

# Run the tkinter event loop
root.mainloop()
