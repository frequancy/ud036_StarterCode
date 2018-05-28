"""a module for creating instances of the "Movie" class"""

import fresh_tomatoes
import media

#instances of my favorite movies
inception = media.Movie("Inception",
        "http://cdn.collider.com/wp-content/uploads/Inception-movie-poster-4.jpg",
        "https://youtu.be/xitHF0IPJSQ")

hard_henry = media.Movie("Hardcore Henry",
        "http://courte-focale.fr/Images/Hardcore%20Henry_affiche.jpg",
        "https://youtu.be/WgyknXk1BRo")

kungfu_panda = media.Movie("KungFu Panda",
        "https://image.tmdb.org/t/p/original/emsYnlA3033Vdl1NGA39VgZGuIB.jpg",
        "https://youtu.be/FQ63rqSRrEI")

theory_of_everything = media.Movie("The Theory Of Everything",
        "http://www.awardsdaily.com/FYC/2014/theory2_big.jpg",
        "https://youtu.be/Salz7uGp72c")

the_conjuring = media.Movie("The Conjuring",
        "http://cdn.collider.com/wp-content/uploads/the-conjuring-uk-poster.jpg",
        "https://youtu.be/k10ETZ41q5o")

whiplash = media.Movie("Whiplash",
        "http://cdn.collider.com/wp-content/uploads/whiplash-poster.jpg",
        "https://youtu.be/MfXemr222ek")

#the list of movies that'll be givin to fresh_tomatoes module
movies = [inception, hard_henry, kungfu_panda, theory_of_everything,
    the_conjuring, whiplash]

fresh_tomatoes.open_movies_page(movies)
