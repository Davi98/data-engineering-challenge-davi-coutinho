from google.cloud import pubsub_v1
from src.utils.log import log
import src.utils.enviroment as env
from src.google.Bigquery import Bigquery


project = env.GOOGLE_CLOUD_PROJECT
subscription_name = env.GOOGLE_CLOUD_SUBSCRIPTION
dataset = env.DATASET
table = env.TABLE

bq = Bigquery(project,dataset,table)
subscriber = pubsub_v1.SubscriberClient()

subscription_path = subscriber.subscription_path(project, subscription_name)

def callback(message):
    """Callback for data stream event listening.
    Every data event submited will be read by this function"""
    try:
        message_data =  message.data.decode('utf8','replace')
        log().debug(f"Loading this data to bigquery: {message_data}")
        bq.insert_row(message_data)
        message.ack()
    except Exception as err:
        log().error(f"Error listening to message {err}")


log().info("Listening for messages on {}".format(subscription_path))
future = subscriber.subscribe(subscription_path, callback)


try:
    future.result()
except KeyboardInterrupt:
    future.cancel()