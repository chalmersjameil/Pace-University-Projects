import json

class Movie:
    def __init__(self, title, year):
        self.title = title 
        self.year = year    
        self.cast = []     
        self.genres = []   
        self.description = None

    def set_description(self, description):
        self.description = description

    def set_cast(self, cast_list):
        if isinstance(cast_list, list):
            self.cast = cast_list
        else:
            raise ValueError("Cast must be a list.")

    def set_genres(self, genres_list):
        if isinstance(genres_list, list):
            self.genres = genres_list
        else:
            raise ValueError("Genres must be a list.")

def main():
    """Read the movies from the file"""
    movies = []
    try:
        with open('data/movies.json', 'r', encoding='utf-8') as f:
            movies_str = f.read()
            movies_json = json.loads(movies_str)
            for movie_json in movies_json:
                movie_title = movie_json['title']
                movie_year = movie_json['year']

                movie = Movie(movie_title, movie_year)

                if 'cast' in movie_json:
                    movie.set_cast(movie_json['cast'])
                if 'genres' in movie_json:
                    movie.set_genres(movie_json['genres'])
                if 'extract' in movie_json:
                    movie.set_description(movie_json['extract'])

                movies.append(movie)

    except FileNotFoundError:
        print("The file 'movies.json' was not found.")
        return
    except json.JSONDecodeError:
        print("Error decoding JSON. Please check the file format.")
        return

    print(len(movies))
    if movies:
        print(f"First movie: {movies[0].title}, {movies[0].year}, {movies[0].description}")

if __name__ == '__main__':
    main()
