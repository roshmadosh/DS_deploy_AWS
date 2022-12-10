from model import generate_model_pickle
from classes import S3


vectorizer = generate_model_pickle()

s3 = S3()
s3.save()

# log_model = pickle.load(open(path_to_file, 'rb'))




# toy_story = pd.Series(['Toy Story'])
# vectorized = vectorizer.transform(toy_story)
#
# print(log_model.predict(vectorized))
