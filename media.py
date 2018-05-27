"""this modul is for constructing a class that defines the movies we're giving
to the web page """

class Movie():
    def __init__(self, movie_title, movie_story, poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_story
        self.poster_img_url = poster_image
        self.trailer_youtube_url = trailer_youtube
