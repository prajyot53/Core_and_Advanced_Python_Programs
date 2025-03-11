class MovieLibrary:
    # Class Attribute
    available_movies = ["Inception", "Interstellar", "The Matrix", "Avengers", "Titanic"]

    def __init__(self, member_name):
        # Instance Attributes
        self.member_name = member_name  # Name of the library member
        self.borrowed_movies = []  # List of borrowed movies

    def borrow_movie(self, movie):
        """
        Method to borrow a movie from the library
        - Checks if the movie is available
        - Adds the movie to the member's borrowed list
        - Removes the movie from the library's available list
        """
        if movie in MovieLibrary.available_movies:
            self.borrowed_movies.append(movie)
            MovieLibrary.available_movies.remove(movie)
            print(f"{self.member_name} borrowed '{movie}'.")
        else:
            print("Movie not available.")

    def return_movie(self, movie):
        """
        Method to return a movie to the library
        - Removes the movie from the member's borrowed list
        - Adds the movie back to the library's available list
        """
        if movie in self.borrowed_movies:
            self.borrowed_movies.remove(movie)
            MovieLibrary.available_movies.append(movie)
            print(f"{self.member_name} returned '{movie}'.")
        else:
            print("This movie was not borrowed.")

    def view_borrowed_movies(self):
        """
        Method to display all movies borrowed by the member
        """
        if self.borrowed_movies:
            print(f"{self.member_name} has borrowed: {', '.join(self.borrowed_movies)}")
        else:
            print("No movies borrowed.")

# Example Usage
member1 = MovieLibrary("Prajyot")
member1.borrow_movie("Inception")
member1.view_borrowed_movies()
member1.return_movie("Inception")
member1.view_borrowed_movies()

"""O/p:-Prajyot borrowed 'Inception'.
Prajyot has borrowed: Inception
Prajyot returned 'Inception'.
No movies borrowed."""