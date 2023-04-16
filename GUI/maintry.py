import tkinter as tk

# Create a function to handle button click events
def on_button_click(choice):
    if choice == 1:
        import new_sim
        print("Thank you for using the IMDB scraper!")
    elif choice == 2:
        # import Topmovies
        # Import the functions or classes from the top movies file
        from topmoviesclone import populate_table

        # Your main file code here

        # Create a button to populate the table
        btn_display = ttk.Button(root, text="Display", command=populate_table)
        btn_display.pack()

        # Rest of your main file code here

        print("Thank you for using the IMDB scraper!")
    elif choice == 3:
        # import Topboxoffice
        from topboxofficeclone import populate_table

        # Create a button to populate the table
        btn_display = ttk.Button(root, text="Display", command=populate_table)
        btn_display.pack()
        
        print("Thank you for using the IMDB scraper!")
    elif choice == 4:
        import Popularmovie
        print("Thank you for using the IMDB scraper!")
    elif choice == 5:
        import Indianmovie
        print("Thank you for using the IMDB scraper!")
    elif choice == 6:
        import movie_search_main
        fptr = open("watchlist.txt", "w")
        print("Do you want to add the movie in your watchlist?")
        print("Press 1 for yes and 0 for no")
        b = int(input())
        if b == 1:
            fptr.write(movie_search_main.name)
        print("Thank you for using the IMDB scraper!")

# Create the main Tkinter window
root = tk.Tk()
root.title("IMDB Scraper")

# Create buttons for each option
button1 = tk.Button(root, text="Sort by Genre", command=lambda: on_button_click(1))
button1.pack(pady=10)

button2 = tk.Button(root, text="Top Movies of All Time", command=lambda: on_button_click(2))
button2.pack(pady=10)

button3 = tk.Button(root, text="Top Box Office Movies this Weekend", command=lambda: on_button_click(3))
button3.pack(pady=10)

button4 = tk.Button(root, text="Most Popular Movies of All Time", command=lambda: on_button_click(4))
button4.pack(pady=10)

button5 = tk.Button(root, text="Indian Movie Database", command=lambda: on_button_click(5))
button5.pack(pady=10)

button6 = tk.Button(root, text="Search Any Movie", command=lambda: on_button_click(6))
button6.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()
