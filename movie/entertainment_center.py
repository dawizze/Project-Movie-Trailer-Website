import media
import fresh_tomatoes

one_punch_man = media.Movie("One Punch Man",
                            "A man who is a hero for fun",
                            "http://static.comicvine.com/uploads/original"+
                            "/11124/111244055/4858488-maxresdefault+(1).jpg",
                            "https://www.youtube.com/watch?v=YUH1mfV3IEU",
                            "PG")

deadpool = media.Movie("Deadpool",
                       "Movie about a man finding his long lost loved one",
                       "https://images-na.ssl-images-amazon.com/images/M/MV5BM"
                       +"jQyODg5Njc4N15BMl5BanBnXkFtZTgwMzExMjE3NzE@._"+
                       "V1_UY268_CR1,0,182,268_AL_.jpg",
                       "https://www.youtube.com/watch?v=ZIM1HydF9UA",
                       "R")

Jason_Bourne = media.Movie("Jason Bourne Ultimatum",
                           "Movie about a man looking for the man with his "+
                           "true identity",
                           "http://www.centerforinquiry.net/images/blog_"+
                           "images/9f59fc42db95ed4ee26a542cb43d3ea3.jpg",
                           "https://www.youtube.com/watch?v=ohkW_xbPl9A",
                           "PG-13")

movies = [one_punch_man, deadpool, Jason_Bourne]
fresh_tomatoes.open_movies_page(movies)
