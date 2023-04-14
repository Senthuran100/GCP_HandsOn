import os
from google.cloud import pubsub_v1

# Insert the project id here
project_id = "##########"
# Insert the topic id here
topic_id = "#############"

def hello_world(request):
    try:
        publisher = pubsub_v1.PublisherClient()
        testAttribute = request.get_json().get('test')
        
        print('Request Param :',testAttribute)
        topic_path = publisher.topic_path(project_id, topic_id)
        data = testAttribute.encode("utf-8")
        future = publisher.publish(topic_path,  data=bytes(data))
        print(future.result())
        return f"OK"
    except Exception as e: 
        print(e)
        return f"Not OK"