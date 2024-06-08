
import json
import random
import sys
from datetime import datetime, timedelta
from time import sleep

from kafka import KafkaProducer

if __name__ == "__main__":
    SERVER = "broker:9092"

    producer = KafkaProducer(
        bootstrap_servers=[SERVER],
        value_serializer=lambda x: json.dumps(x).encode("utf-8"),
        api_version=(3, 7, 0),
    )
    
    try:
        while True:
            
            t = datetime.now() + timedelta(seconds=random.randint(-15, 0))
            
            message = {
                "time" : str(t),
                "id" : random.choice(["a", "b", "c", "d", "e"]),
                "values" : random.randint(0,100)
            }
            
            
            producer.send("bobry", value=message)
            sleep(1)
    except KeyboardInterrupt:
        producer.close()
