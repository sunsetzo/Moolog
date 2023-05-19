import requests
import json

TMDB_API_KEY = 'be22ff2ea45ab37ba4186006a5a150c5'

def get_movie_datas():
    total_data = []

    #### 현재 상영작 데이터 가져오기 ####
    now_playing_movies_cnt = 0
    request_url = f"https://api.themoviedb.org/3/movie/now_playing?api_key={TMDB_API_KEY}&language=ko-KR&page=1"
    movies = requests.get(request_url).json()

    for movie in movies['results']:
        if movie.get('release_date', ''):
            fields = {
                # 'movie_id': movie['id'],
                'title': movie['title'],
                'release_date': movie['release_date'],
                'popularity': movie['popularity'],
                'vote_avg': movie['vote_average'],
                'vote_count': movie['vote_count'],
                'overview': movie['overview'],
                'poster_path': movie['poster_path'],
                'backdrop_path':movie['backdrop_path'],
                'genres': movie['genre_ids']
            }

            data = {
                "pk": movie['id'],
                "model": "movies.movie",
                "fields": fields
            }

            now_playing_movies_cnt += 1
            total_data.append(data)
    
    #### 개봉 예정작 데이터 가져오기 ####
    upcoming_movies_cnt = 0
    request_url = f"https://api.themoviedb.org/3/movie/upcoming?api_key={TMDB_API_KEY}&language=ko-KR&page=1"
    movies = requests.get(request_url).json()

    for movie in movies['results']:
        if movie.get('release_date', ''):
            fields = {
                # 'movie_id': movie['id'],
                'title': movie['title'],
                'release_date': movie['release_date'],
                'popularity': movie['popularity'],
                'vote_avg': movie['vote_average'],
                'vote_count': movie['vote_count'],
                'overview': movie['overview'],
                'poster_path': movie['poster_path'],
                'backdrop_path':movie['backdrop_path'],
                'genres': movie['genre_ids']
            }

            data = {
                "pk": movie['id'],
                "model": "movies.movie",
                "fields": fields
            }

            upcoming_movies_cnt += 1
            total_data.append(data)

    #### 인기있는 영화 데이터 가져오기 ####

    for i in range(1, 10):
        request_url = f"https://api.themoviedb.org/3/movie/popular?api_key={TMDB_API_KEY}&language=ko-KR&page={i}"
        movies = requests.get(request_url).json()
        
        for movie in movies['results']:
            if movie.get('release_date', ''):
                fields = {
                    # 'movie_id': movie['id'],
                    'title': movie['title'],
                    'release_date': movie['release_date'],
                    'popularity': movie['popularity'],
                    'vote_avg': movie['vote_average'],
                    'vote_count': movie['vote_count'],
                    'overview': movie['overview'],
                    'poster_path': movie['poster_path'],
                    'backdrop_path':movie['backdrop_path'],
                    'genres': movie['genre_ids']
                }

                data = {
                    "pk": movie['id'],
                    "model": "movies.movie",
                    "fields": fields
                }

                total_data.append(data)

    print(f'현재 상영작 영화 개수 : {now_playing_movies_cnt}개, 개봉 예정작 영화 개수 : {upcoming_movies_cnt}개')

    with open("movies/fixtures/movie_data.json", "w", encoding="utf-8") as w:
        json.dump(total_data, w, indent=4, ensure_ascii=False)


def get_genre_data():
    total_data = []

    request_url = f"https://api.themoviedb.org/3/genre/movie/list?api_key={TMDB_API_KEY}"
    genres = requests.get(request_url).json()

    for genre in genres['genres']:
        fields = {
            # 'genre_id': genre['id'],
            'name': genre['name'],
        }

        data = {
            "pk": genre['id'],
            "model": "movies.genre",
            "fields": fields
        }
        total_data.append(data)

    with open("movies/fixtures/genre_data.json", "w", encoding="utf-8") as w:
        json.dump(total_data, w, indent=4, ensure_ascii=False)

get_movie_datas()
get_genre_data()

'''
movies/fixtures/ 만들고

python init.py 

python manage.py migrate

python manage.py loaddata genre_data.json movie_data.json

'''