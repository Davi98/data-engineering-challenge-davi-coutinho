from distutils.debug import DEBUG
import os
DEBUG = os.environ['DEBUG'] if 'DEBUG' in os.environ else False
GOOGLE_CLOUD_PROJECT =  os.environ['GOOGLE_CLOUD_PROJECT'] if 'GOOGLE_CLOUD_PROJECT' in os.environ else "streamingsdata"
GOOGLE_CLOUD_SUBSCRIPTION =  os.environ['GOOGLE_CLOUD_SUBSCRIPTION'] if 'GOOGLE_CLOUD_SUBSCRIPTION' in os.environ else "challenge-sub"
DATASET = os.environ['DATASET'] if 'DATASET' in os.environ else "challenge"
TABLE = os.environ['DATASET'] if 'DATASET' in os.environ else "trips"
