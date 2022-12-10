import pandas as pd


def get_data():
    movies_df = pd.read_csv('~/brainstation/capstone/DS_deploy_AWS/sagemaker/movies.csv')
    ratings_df = pd.read_csv('~/brainstation/capstone/DS_deploy_AWS/sagemaker/ratings.csv')
    return movies_df, ratings_df

