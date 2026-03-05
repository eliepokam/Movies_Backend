# %%
from database import SessionLocal
from query_helpers import *

db = SessionLocal()

# %%
movie = get_movie(db , movie_id=1)
print(movie.title , movie.genres)

db.close()

# %%
movies = get_movies(db , limit=5)
for film in movies :
    print(f"ID : {film.movieId} , Titre : {film.title} , Genres : {film.genres}")
# %%
rating = get_rating(db , movie_id=1 , user_id=1)
print(f"User ID : {rating.userId} , Movie ID :{rating.movieId} , Rating :{rating.rating} , Timestamp : {rating.timestamp}")
# %%
ratings = get_ratings(db , min_rating=3.5 , limit=10)
for film in ratings :
    print(f"ID : {film.movieId} , Note : {film.rating}")

 # %%
n_movies = get_movie_count(db)
print(f"Nombres de films : {n_movies}")
# %%
total_tag = get_tag_count(db)
print(f"Nombre de tags : {total_tag}")
# %%
total_link = get_link_count(db)
print(f"Nombre de tags : {total_tag}")
# %%
