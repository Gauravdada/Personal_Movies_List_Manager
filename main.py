movies = []

def menu():
    user_input = input("Enter 'a' to add movie, 'l' to see your movies, 'f' to find movie, 'q' to quit: ")

    while user_input != 'q':
        if user_input == 'a':
            add_movie()
        elif user_input == 'l':
            show_movies(movies)
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


def show_movies(movie_list):
    for movie in movies:
        show_movie_list(movie)

        
def show_movie_list(movie):
    print(f"Name :- {movie['Name']} ")
    print(f"Type :- {movie['Type']}")
    print(f"Rating :- {movie['Rating']}")
    print("")


def find_movie():
    find_by = input("What property of movie are you looking for : ")
    looking_for = input("What are you searching for : ")

    found_movies = find_by_attributes(movies, looking_for, lambda x: x[find_by])
    
    
def find_by_attributes(item, expected, finder)
    found = []

    for i in items:
      if finder(i) == expected:
        found.append(i)
  
    return found

menu()