import webbrowser

class Movie():
    """ This class provides a way to store movie related information """

    # valid ratings for each movie
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]

    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube, rating):
        """ The init function will take in the title, move storyline, image,
            trailer, and rating inorder to initialize the moive instance
            - Image will be used as a thumbnail
            - Trailer link will be used to show the movies trailer """

        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.rating = rating

    # Shows the trailer for the movie
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
