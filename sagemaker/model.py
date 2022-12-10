import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression

# *** IMPORT DATA ***
movies_df = pd.read_csv('~/brainstation/capstone/DS_deploy_AWS/sagemaker/movies.csv')
ratings_df = pd.read_csv('~/brainstation/capstone/DS_deploy_AWS/sagemaker/ratings.csv')

# merge dataframes
df = pd.merge(ratings_df, movies_df, how='inner', on='movieId')

# remove features that won't be included in our logit
df = df.drop(['userId', 'movieId', 'timestamp'], axis=1)

'''cross reference original df to get genres for each movie. we're doing this
because groupby will remove non numeric columns.'''
DELIMITER = "hiroshisdelimeter"
cross_ref = df['title'] + [DELIMITER] + df['genres']
genres_column = [row.split(DELIMITER) for row in cross_ref.unique()]
genres_df = pd.DataFrame(genres_column, columns=['title', 'genres'])

# group by title and get the mean rating for each movie
df = df.groupby('title').mean()

# merge genres column with grouped dataframe
df = df.merge(genres_df, how='inner', on='title')
print(df)

# create list of unique genres
genres_array = np.array([genres.split('|') for genres in df['genres']])
flattened_genre_array = genres_array.flatten()
flattened_more = [genre[0] for genre in flattened_genre_array]

unique_genres = set(flattened_more)

# create a list of genre one hot encodings
genre_OHEs = list()
for row in genres_array:
    genre_OHE = [1 if genre in row else 0 for genre in unique_genres]
    genre_OHEs.append(genre_OHE)

# convert genre one hot encodings to dataframe
genres_df = pd.DataFrame(genre_OHEs, columns=list(unique_genres))


# merge genre OHEs to original dataframe
df = pd.concat((df, genres_df), axis=1)
print(df.loc[0, :])

# *** MODEL ***






