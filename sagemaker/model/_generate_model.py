from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import pickle


def generate_model(df):
    """
        This model will try to predict the rating of a movie based on its title.
    """
    X = df.iloc[:400, 2:]
    y = df.iloc[:400, 1]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.2)

    log_reg = LogisticRegression()
    log_reg.fit(X_train, y_train)
    train_score = log_reg.score(X_train, y_train)
    test_score = log_reg.score(X_test, y_test)

    print("**********SCORES**************")
    print('train: {:.2f} test: {:.2f}'.format(train_score, test_score))
    print("******************************")
    pickle.dump(log_reg, open('my_model.pickle', 'wb'))

