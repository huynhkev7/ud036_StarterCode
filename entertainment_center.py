import fresh_tomatoes
import media

# Create 6 Movie instances to store their title, poster image, and trailer link
avengers = media.Movie(
    "Avengers: Infinity War",
    "https://upload.wikimedia.org/wikipedia"
    "/en/4/4d/Avengers_Infinity_War_poster.jpg",
    "https://www.youtube.com/watch?v=QwievZ1Tx-8"
    )

titanic = media.Movie(
    "Titanic",
    "https://upload.wikimedia.org/wikipedia"
    "/en/2/22/Titanic_poster.jpg",
    "https://www.youtube.com/watch?v=zCy5WQ9S4c0"
    )

naruto = media.Movie(
    "The Last: Naruto the Movie",
    "https://upload.wikimedia.org/wikipedia"
    "/en/thumb/0/0c/TheLastNarutomovie.jpg"
    "/220px-TheLastNarutomovie.jpg",
    "https://www.youtube.com/watch?v=mksl3tYdyK4"
    )

captain_america = media.Movie(
    "Captain America: The First Avenger",
    "https://upload.wikimedia.org/wikipedia/"
    "en/3/37/Captain_America_The_First_Avenger_poster.jpg",
    "https://www.youtube.com/watch?v=JerVrbLldXw"
    )

pacific_rim = media.Movie(
    "Pacific Rim",
    "https://upload.wikimedia.org/wikipedia/"
    "en/f/f3/Pacific_Rim_FilmPoster.jpeg",
    "https://www.youtube.com/watch?v=5guMumPFBag"
    )

snowden = media.Movie(
    "Snowden",
    "https://upload.wikimedia.org/wikipedia/"
    "en/c/ca/Snowden_film_poster.jpg",
    "https://www.youtube.com/watch?v=QlSAiI3xMh4"
    )

# Store the Movie instances in a list to be displayed on webpage
movies = [
    avengers, titanic,
    naruto, captain_america,
    pacific_rim, snowden
    ]

# Generate a webpage that showcases the favorite movies given in list
fresh_tomatoes.open_movies_page(movies)
