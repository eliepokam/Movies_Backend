# %%
from database import SessionLocal
from models import Movie, Rating , Tag, Link 

db = SessionLocal()

# %% Tester la récupération de quelques films
movies = db.query(Movie).limit(5).all()
for movie in movies :
    print(movie.movieId , movie.title , movie.genres)
else :
    print('No film found')
# %%
ratings = db.query(Rating).limit(5).all()

if ratings:
    for rating in ratings:
        print(f"User {rating.userId} a noté le film {rating.movieId} avec {rating.rating}/5")
else:
    print("Aucune évaluation trouvée.")
# %%
ratings = db.query(Rating).limit(5).all()

if ratings:
    for rating in ratings:
        print(f"User {rating.userid} a noté le film {rating.movieId} avec {rating.rating}/5")
else:
    print("Aucune évaluation trouvée.")
# %%
high_rated_movies = (
    db.query(Movie.title, Rating.rating)
    .join(Rating, Movie.movieId == Rating.movieId)
    .filter(Rating.rating >= 4.0)
    .limit(5)
    .all()
)

if high_rated_movies:
    for title, rating in high_rated_movies:
        print(f"Film: {title}, Note: {rating}/5")
else:
    print("Aucun film avec une note >= 4 trouvé.")

# %% Fermer la session
db.close()

# %%
