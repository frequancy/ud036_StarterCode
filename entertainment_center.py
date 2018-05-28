"""a module for creating instances of the "Movie" class"""

import fresh_tomatoes
import media

inception = media.Movie("Inception", "http://cdn.collider.com/wp-content/uploads/\
Inception-movie-poster-4.jpg", "https://youtu.be/xitHF0IPJSQ")

hard_henry = media.Movie("Hardcore Henry", "http://courte-focale.fr/Images/Hard\
core%20Henry_affiche.jpg", "https://youtu.be/WgyknXk1BRo")

kungfu_panda = media.Movie("KungFu Panda", "https://de1imrko8s7v6.cloudfront.net/\
movies/posters/kungfupanda-3_1435178111.jpg", "https://youtu.be/FQ63rqSRrEI")

theory_of_everything = media.Movie("The Theory Of Everything", "http://www.blackfilm\
.com/read/wp-content/uploads/2014/10/The-Theory-of-Everything-Poster-2.jpg",
"https://youtu.be/Salz7uGp72c")

the_conjuring = media.Movie("The Conjuring", "http://images.cinemas-online.co.uk/0/\
4/82/CONJURING_ONESHEET_MAIN_FINAL_INTL-5807.JPG", "https://youtu.be/k10ETZ41q5o")

whiplash = media.Movie("Whiplash", "http://cdn.collider.com/wp-content/\
uploads/whiplash-poster.jpg", "https://youtu.be/MfXemr222ek")

movies = [inception, hard_henry, kungfu_panda, theory_of_everything,
    the_conjuring, whiplash]
    
fresh_tomatoes.open_movies_page(movies)
