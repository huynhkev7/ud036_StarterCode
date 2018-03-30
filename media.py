class Movie(object):
    """
    Class to stores common properties related to a movie.
    Attributes:
        title: The title of the movie
        poster_image_url: The poster image link for the movie from Wikipedia
        trailer_youtube_url: The link to the movie trailer on Youtube
    """
    def __init__(self, title, poster_image_url, trailer_youtube_url):
        self.title = title
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
