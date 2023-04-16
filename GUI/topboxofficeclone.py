import requests
from bs4 import BeautifulSoup
import pandas as pd
import tkinter as tk
from tkinter import ttk
from tabulate import tabulate

# Create main window
root = tk.Tk()
root.title("IMDb Box Office Chart")

# Create a Treeview widget
tree = ttk.Treeview(root, columns=(
    "Title", "Weekend", "Total Gross", "Weeks", "Link"), show="headings")

# Add column headings
tree.heading("Title", text="Title")
tree.heading("Weekend", text="Weekend")
tree.heading("Total Gross", text="Total Gross")
tree.heading("Weeks", text="Weeks")
tree.heading("Link", text="Link")

# Define a function to populate the table


def populate_table():

    # Clear existing data in the table
    tree.delete(*tree.get_children())

    # Get data from IMDb website
    topics_url = 'https://www.imdb.com/chart/boxoffice/'
    response = requests.get(topics_url)
    if response.status_code != 200:
        raise Exception(f"Failed to load page {response}")
    page_contents = response.content
    soup = BeautifulSoup(page_contents, 'html5lib')

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

    def title_column():
        title_l = extractor("titleColumn", "td")
        movie_name = []
        for i in title_l:
            l = i.split("\n")
            n1 = l[0].rstrip()
            movie_name.append(n1)
        return movie_name

    def weekend_column():
        l = []
        selection_class = 'ratingColumn'
        topic_title_tags = soup.find_all('td', {'class': selection_class})
        j = 0
        for i in topic_title_tags:
            new = i.text.strip()
            if j % 2 == 0:
                l.append(new)
            j += 1
        return l

    def gross_column():
        gross_l = extractor("secondaryInfo", "span")
        return gross_l

    def link():
        base_link = "https://www.imdb.com"
        selection_class = "titleColumn"
        topic_title_tags = soup.find_all("td", {'class': selection_class})
        link_l = []
        for i in topic_title_tags:
            link = i.find('a')['href']
            link_l.append(base_link + link)
        return link_l

    def weeks_column():
        weeks_l = extractor("weeksColumn", "td")
        return weeks_l

    data_dict = {'Movie Name': title_column(),
                 'Weekend': weekend_column(),
                 'Gross': gross_column(),
                 'Weeks': weeks_column(),
                 'Link': link()
                 }
    df = pd.DataFrame(data_dict)

    # Add data to the table
    for row in df.itertuples(index=False):
        tree.insert("", "end", values=row)


# Create a button to populate the table
btn_display = ttk.Button(root, text="Display", command=populate_table)
btn_display.pack()


def update_table_sort(*args):
    populate_table()


# Create a scrollbar for the table
scrollbar = ttk.Scrollbar(root, orient="vertical", command=tree.yview)
scrollbar.pack(side="right", fill="y")
tree.configure(yscrollcommand=scrollbar.set)


# Pack the treeview widget
tree.pack(expand="yes", fill="both")

# Run the main window
root.mainloop()
