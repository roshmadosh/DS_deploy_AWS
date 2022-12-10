from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import pickle
import os
from dotenv import load_dotenv
from . import get_data, generate_df

load_dotenv()


PATH_TO_MODEL = os.getenv('PATH_TO_MODEL')


def generate_model_pickle():
    if not os.path.exists(PATH_TO_MODEL):
        print('Generating model...')

        movies_df, ratings_df = get_data()
        df, vectorizer = generate_df(movies_df=movies_df, ratings_df=ratings_df)
        log_model = _create_model_from_df(df)

        # writing model to pickle
        pickle.dump(log_model, open(PATH_TO_MODEL, 'wb'))

        # returning vectorizer for generating predictions with transform()
        return vectorizer


def _create_model_from_df(df):
    """
        This model will try to predict the rating of a movie based on its title.
    """
    X = df.iloc[:, 2:]
    y = df.iloc[:, 1]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.2)

    log_reg = LogisticRegression()
    log_reg.fit(X_train, y_train)
    train_score = log_reg.score(X_train, y_train)
    test_score = log_reg.score(X_test, y_test)

    print("**********SCORES**************")
    print('train: {:.2f} test: {:.2f}'.format(train_score, test_score))
    print("******************************")
    return log_reg
