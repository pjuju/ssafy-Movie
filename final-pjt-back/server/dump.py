import urllib.request
from pprint import pprint
import json

API_KEY = "e97617d64b251b650b844ce38f163eaa"
HOST = "https://api.themoviedb.org"
POPULAR_LIST_URI = "/3/movie/popular"
NOW_PLAYING_LIST_URI = "/3/movie/now_playing"
LATEST = "/3/movie/latest"
UPCOMING_LIST_URI = "/3/movie/upcoming"
TOP_LATED_URI = "/3/movie/top_rated"
MOVIE_INFO_URI = "/3/movie/"
GENRE_LIST_URI = "/3/genre/movie/list"
MOVIE_URI_LIST =[POPULAR_LIST_URI,NOW_PLAYING_LIST_URI,LATEST,UPCOMING_LIST_URI,TOP_LATED_URI]

movie_list = []
movie_Ids = []
genre_list = []

genre_request = (f'{HOST}{GENRE_LIST_URI}?api_key={API_KEY}&language=ko')
response = urllib.request.urlopen(genre_request)
json_str = response.read().decode('utf-8')
json_object = json.loads(json_str)

genre_data = json_object.get("genres")

for data in genre_data:

    my_data = {
        "number": data.get("id"),
        "name": data.get("name")
    }

    my_genre = {
        "model": "movies.genre",
        "pk": my_data.get("number"),
        "fields": {
            "name": my_data.get("name")
        },
    }
    genre_list.append(my_genre)



for MOVIE_URI in MOVIE_URI_LIST:
    for i in range(1, 50):
        request = (f'{HOST}{MOVIE_URI}?api_key={API_KEY}&language=ko&page={i}')
        response = urllib.request.urlopen(request)
        json_str = response.read().decode('utf-8')
        json_object = json.loads(json_str)

        if not json_object.get("results"):
            break

        data_movies = (json_object.get("results"))
        for movie in data_movies:
            if movie.get("id") not in movie_Ids:
                movie_Ids.append(movie.get("id"))

for idx, movie_Id in enumerate(movie_Ids):
    movie_request = (f'{HOST}{MOVIE_INFO_URI}{movie_Id}?api_key={API_KEY}&language=ko&')
    response = urllib.request.urlopen(movie_request)
    json_str = response.read().decode('utf-8')
    json_object = json.loads(json_str)
    if json_object.get("poster_path"):
        if json_object.get("genres"):

            my_object = {
                "model": "movies.movie",
                "pk": idx+1,                
                "fields": {
                    "tmdb_id": movie_Id,
                    "title": json_object.get("title"),
                    "adult": json_object.get("adult"),
                    "popularity": json_object.get("popularity"),
                    "poster_path": json_object.get("poster_path"),
                    "release_date": json_object.get("release_date"),
                    "runtime": json_object.get("runtime"),
                    "vote_average": json_object.get("vote_average"),
                    "vote_count": json_object.get("vote_count"),
                    "overview": json_object.get("overview"),
                    "genres": [json_object.get("genres")[0].get("id")],
                    "original_title": json_object.get("original_title"),
                }  
            }
        else:
            my_object = {
                "model": "movies.movie",
                "pk": idx+1,
                "movie_id": movie_Id,
                "fields": {
                    "title": json_object.get("title"),
                    "adult": json_object.get("adult"),
                    "popularity": json_object.get("popularity"),
                    "poster_path": json_object.get("poster_path"),
                    "release_date": json_object.get("release_date"),
                    "runtime": json_object.get("runtime"),
                    "vote_average": json_object.get("vote_average"),
                    "vote_count": json_object.get("vote_count"),
                    "overview": json_object.get("overview"),
                    "genres": json_object.get("genres"),
                    "original_title": json_object.get("original_title"),
                }
            }
        movie_list.append(my_object)

with open('movies.json', 'w', encoding='UTF-8') as file:
    file.write(json.dumps(movie_list, ensure_ascii=False))

with open('genres.json', 'w', encoding='UTF-8') as file:
    file.write(json.dumps(genre_list, ensure_ascii=False))
