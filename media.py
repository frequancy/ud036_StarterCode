"""this modul is for constructing a class that defines the specification of
movies we're giving to the web page """

import webbrowser

class Movie():
    def __init__(self, movie_title, poster_image, trailer_youtube):
        self.title = movie_title
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.poster_img_url)
