import pandas as pd
import numpy as np
import re
from sklearn.feature_extraction.text import CountVectorizer


def generate_df(**kwargs):
    movies_df = kwargs.get('movies_df', None)
    ratings_df = kwargs.get('ratings_df', None)

    # input validation
    assert movies_df is not None, 'A "movies_df" kwarg is not present.'
    assert ratings_df is not None, 'A "ratings_df" kwarg is not present.'

    # merge dataframes, remove features
    df = pd.merge(movies_df, ratings_df, how='inner', on='movieId') \
        .drop(['userId', 'movieId', 'timestamp'], axis=1) \

    # reassigning title to get rid of duplicates
    titles, years = _generate_title_without_year(list(df['title']))
    df['title'] = titles
    # df['year'] = years

    # group by ratings
    df = _groupby_avg_ratings(df)

    # get tokenized df, vectorizer for transforming predictions
    tokens_df, vectorizer = _generate_tokens_df(pd.Series(titles).unique())

    # assign features to dataframe
    df = pd.concat([df, tokens_df], axis=1)

    # since our model will categorize by rating
    df['rating'] = df['rating'].apply(lambda x: _map_to_categorical(x))

    return df, vectorizer

def _map_to_categorical(rating):
    return str(int(round(rating)))

def _generate_title_without_year(titles):
    new_titles = list()
    years = list()
    for title in titles:
        search = re.search(r"\([0-9]{4}\)", title)
        year = int(search.group()[1:5]) if search else None
        new_title = title[:search.endpos - 7] if search is not None else title
        new_titles.append(new_title)
        years.append(year)
    return new_titles, years

def _generate_tokens_df(titles):
    vectorizer = CountVectorizer(analyzer='word', stop_words='english')
    tokens = vectorizer.fit_transform(titles).todense()
    return pd.DataFrame(tokens, columns=vectorizer.get_feature_names_out()), vectorizer


def _groupby_avg_ratings(df):
    # group by title and get the mean rating for each movie
    return df.groupby('title').mean().reset_index()


def _generate_genres_df(df):
    '''cross reference original df to get genres for each movie. we're doing this
    because groupby will remove non numeric columns.'''
    delimiter = "hiroshisdelimeter"
    cross_ref = df['title'] + [delimiter] + df['genres']
    genres_column = [row.split(delimiter) for row in cross_ref.unique()]
    return pd.DataFrame(genres_column, columns=['title', 'genres'])


def __generate_ohe_df(df):
    # create list of unique genres
    genres_array = np.array([genres.split('|') for genres in df['genres']])
    flattened_genre_array = genres_array.flatten()
    flattened_more = [genre[0] for genre in flattened_genre_array]
    unique_genres = set(flattened_more)

    # create a list of genre one hot encodings
    genre_ohes = list()
    for row in genres_array:
        genre_ohe = [1 if genre in row else 0 for genre in unique_genres]
        genre_ohes.append(genre_ohe)

    # convert genre one hot encodings to dataframe
    return pd.DataFrame(genre_ohes, columns=list(unique_genres)), unique_genres

