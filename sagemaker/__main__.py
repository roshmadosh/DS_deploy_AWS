import pandas as pd
from model import get_data, generate_df, generate_model
import os.path
import pickle
movies_df, ratings_df = get_data()
df, vectorizer = generate_df(movies_df=movies_df, ratings_df=ratings_df)

path_to_file = './my_model.pickle'
if not os.path.exists(path_to_file):
    print('Generating model...')
    generate_model(df)

log_model = pickle.load(open(path_to_file, 'rb'))
toy_story = pd.Series(['Toy Story'])
vectorized = vectorizer.transform(toy_story)

print(log_model.predict(vectorized))
