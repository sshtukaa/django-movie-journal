import requests
def get_watched_movies(user, data):
    if data is None:
        return None
    watched_movies = set(user.userprofile.watched_movies.values_list('movie_id', flat=True))
    if "Search" in data:
        for movie in data['Search']:
            movie['watched'] = movie['imdbID'] in watched_movies
    else:
        data['watched'] = data['imdbID'] in watched_movies
    return data
def omdbresponse(text, key="s", API ="400bc237"):
    return requests.get(f"http://www.omdbapi.com/?apikey={API}&{key}={text}")