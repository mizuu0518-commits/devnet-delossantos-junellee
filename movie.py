"""
Midterm Practical Exam — Movie Collection Manager
#Student: [Junelle Delos Santos]
"""

movies = {"Movie Title1: " : "Inception",
          "Director1" : "Christopher Nolan",
          "Movie Status1" : "Watched",
          "Movie Title2" : "Interstellar",
          "Director2" : "Christopher Nolan",
          "Movie Status2" : "Unwatched",
          "Movie Title3" : "The Matrix",
          "Director3" : "Lana Wachowski",
          "Movie Status3" : "Watched"}
menu = ["1. Add Movie", "2. View all movies", "3. Count watched vs unwatched", "4. Find a movie", "5. Exit"]

def display_menu():
    print(menu)
    user_choice = (input("Choose an option: "))
    for user in user_choice:
     if(user_choice == 1):
        add_movie()
     elif(user_choice == 2):
        view_movies()
     elif(user_choice == 3):
         count_watched_unwatched()
     elif(user_choice == 4):
         find_movie()
     else:
        break 
display_menu()

def add_movie(movies):
    movie_title = (input("Enter movie title: "))
    director = (input("Enter movie director: "))
    status = (input("Enter movie status: "))
    # ask for title, director, and status
    # build the movie string
    # add it to the list
    
    movies["New Movie"] = movie_title
    movies["Movie Director"] = director
    movies["Status"] = status
    print(movies)
add_movie(movies)


def view_movies(movies):
    # loop through and print every movie
    # handle empty list
        print(movies)
view_movies(movies)


def count_watched_unwatched(movie_list):
    # loop through the list
    # count Watched vs Unwatched
    # return both counts
    pass


def find_movie(movie_list):
    # ask for a movie title
    # search the list
    # search should be case-insensitive
    # print the result or "Movie not found."
    pass


def main():
    # create the main menu loop
    # call the appropriate function based on the user's choice
    pass


main()
