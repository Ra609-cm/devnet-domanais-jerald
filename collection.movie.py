movies = [
]
 
def display_menu():
print("=== Movie Collection Manager ===")
print("1. Add a movie")
print("2. View all movies")
print("3. Count watched vs unwatched")
print("4.Find a movie")
print("5. Exit")
 
 
 
def add_movie(movie_list):
    tn = str(input("Enter Movie Title:"))
    dr = int(input("Director Name: "))
    stats = str(input("Enter Status: "))
 
 
    add_movie.append(tn,dr,stats)
    movies.extend(movie_list)
 
 
def view_movies(movie_list):
    for x in movies:
    print(x)
 
 
def count_watched_unwatched(movie_list):
    # loop through the list
    # count Watched vs Unwatched
    # return both counts
    pass
 
 
def find_movie(movie_list):
    find = str(input("Enter movie that you want to find "))
    # search the list
    # search should be case-insensitive
    # print the result or "Movie not found."
    pass
 
 
def main():
running = True
    while running:
        choice = display_menu()
        answer = input("Enter your choice: ")
    if answer == 1:
        add_movie()
    elif answer == 2:
        view_movies()
    elif answer == 3:
        count_active_inactive()
    elif answer == 4:
        find_movie()
    elif answer == 5:
        remove_movie()
    elif answer == 6:

 
 
   
    pass
 
 
main()
