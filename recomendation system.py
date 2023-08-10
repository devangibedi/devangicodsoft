from surprise import Dataset, Reader, KNNBasic
import pandas as pd

data = {
    'User1': {'Movie1': 5, 'Movie2': 3, 'Movie3': 4, 'Movie4': 4},
    'User2': {'Movie1': 3, 'Movie2': 1, 'Movie3': 2, 'Movie4': 3},
    'User3': {'Movie1': 4, 'Movie2': 3, 'Movie3': 4, 'Movie4': 3},
    'User4': {'Movie1': 3, 'Movie2': 3, 'Movie3': 1, 'Movie4': 5},
    'User5': {'Movie1': 4, 'Movie2': 4, 'Movie3': 5, 'Movie4': 4},
}

df = pd.DataFrame(data)

reader = Reader(rating_scale=(1, 5))
ratings = []
for user, movies in data.items():
    for movie, rating in movies.items():
        ratings.append((user, movie, rating))
surprise_data = Dataset.load_from_df(pd.DataFrame(ratings, columns=['user', 'item', 'rating']), reader)

sim_options = {
    'name': 'cosine',
    'user_based': False 
}
model = KNNBasic(sim_options=sim_options)

trainset = surprise_data.build_full_trainset()
model.fit(trainset)

def get_movie_recommendations(user, model, df):
    movie_names = df.columns.tolist()

    user_index = trainset.to_inner_uid(user)

    movies_to_predict = [i for i in range(trainset.n_items) if trainset.ur[user_index, i] == 0]

    predictions = [model.predict(user, movie_names[movie_id]).est for movie_id in movies_to_predict]

    top_movie_indices = sorted(range(len(movies_to_predict)), key=lambda i: predictions[i], reverse=True)[:5]

    recommended_movies = [movie_names[movies_to_predict[i]] for i in top_movie_indices]

    return recommended_movies

user = 'User1'
recommendations = get_movie_recommendations(user, model, df)

print(f"Movie recommendations for {user}:")
print(recommendations)
