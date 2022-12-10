import pandas as pd
from model import get_data, generate_df, generate_model
import os
from classes import S3


movies_df, ratings_df = get_data()
df, vectorizer = generate_df(movies_df=movies_df, ratings_df=ratings_df)
log_model = generate_model(df)


s3 = S3()
s3.save(log_model)

# log_model = pickle.load(open(path_to_file, 'rb'))




# toy_story = pd.Series(['Toy Story'])
# vectorized = vectorizer.transform(toy_story)
#
# print(log_model.predict(vectorized))
