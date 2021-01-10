import requests


def get_popular_movies():
    url = "https://api.themoviedb.org/3/movie/popular"
    api_token = "edea2f9c4feb8615385e742ce4c65734"
    headers = {
        "Authorization": f"Bearer {api_token}"
    }
    response = requests.get(url, headers=headers)
    return response.json()

get_popular_movies()

def get_poster_url(poster_path, size="w342"):
    base_url = "https://image.tmdb.org/t/p/"
    return f"{base_url}{size}/{poster_path}"

def get_movie_info():
    dict = { "title" : "url"}
    return dict

def get_movies(how_many):
    data = get_popular_movies()
    return data["results"][:how_many]

#@app.context_processor
def utility_processor():
    def tmdb_image_url(path, size):
        return tmdb_client.get_poster_url(path, size)
    return {"tmdb_image_url": tmdb_image_url}

