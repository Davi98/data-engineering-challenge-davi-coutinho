from google.api_core import exceptions
from google.cloud import pubsub_v1
import json
from src.utils.log import log
from google.api_core.exceptions import AlreadyExists


class Publisher:

    __publisher = ''
    __topic = None

    def __init__(self, topic_name, project_id):
        self.__topic_name = f"projects/{project_id}/topics/{topic_name}"
        self.__publisher = pubsub_v1.PublisherClient()
        try:
            self.__topic = self.__publisher.create_topic(name = self.__topic_name)
            log().info(f'Topic created: {self.__topic}')
        except AlreadyExists as alerr:
            log().debug(f"Topic {self.__topic} already exists: {alerr}")
        except Exception as err:
            log().info(f"Failed connecting to topic with error {err}")

    def publish(self, data):
        json_message = json.dumps(data,ensure_ascii=False)
        try:
            self.__publisher.publish(self.__topic_name, json_message.encode())
            log().debug(f"Message {json_message} sent to topic {self.__topic_name}")
            return True
        except Exception as e:
            log().error(f"Failed sending message {json_message} with error {e}")
            raise
            