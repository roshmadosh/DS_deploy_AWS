import boto3
import pickle
import os
from dotenv import load_dotenv

load_dotenv()

S3_BUCKET = os.getenv('S3_BUCKET')
PATH_TO_MODEL = os.getenv('PATH_TO_MODEL')


class S3:
    def __init__(self):
        self.client = boto3.client('s3')

    def save(self, model):
        if not os.path.exists(PATH_TO_MODEL):
            print('Generating model...')
            pickle.dump(model, open(PATH_TO_MODEL, 'wb'))

        with open(PATH_TO_MODEL, "rb") as f:
            self.client.upload_fileobj(f, S3_BUCKET, "my_model.pickle")
            print('Saved to S3 successful.')
