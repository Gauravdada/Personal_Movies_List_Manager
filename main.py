movies = []

def menu():
    user_input = input("Enter 'a' to add movie, 'l' to see your movies, 'f' to find movie, 'q' to quit: ")

    while user_input != 'q':
        if user_input == 'a':
            add_movie()
        elif user_input == 'l':
            show_movies()
        elif user_input == 'f':
            find_movie()
        else:
            print("Wrong input, try again")

        user_input = input("Enter 'a' to add movie, 'l' to see your movies, 'f' to find movie, 'q' to quit: ")


def add_movie():
    name = input("Enter movie name : ")
    type = input("Enter type of movie : ")
    rating = int(input("Enter your personal Rating : "))

    movies.append({
        'Name' : name,
        'Type' : type,
        'Rating' : rating,
    })


def show_movies():
    for movie in movies:
        show_movie_list(movie)

        
def show_movie_list(movie):
    print(f"Name :- {movie['name']} ")
    print(f"Type :- {movie['type']}")
    print(f"Rating :- {movie['rating']}")
    print("")


menu()