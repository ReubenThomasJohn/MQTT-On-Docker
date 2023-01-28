from mqtt_device import MQTT_Device
from random import random
from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()



# Set up client for MongoDB
# mongoClient=MongoClient("mongodb://localhost:27017/")
connection_string = os.getenv('MONGO_CONNECTION_STRING')
mongoClient=MongoClient(connection_string)
db=mongoClient.SensorData
collection=db.sensor1

connected = False
MessageReceived = False

broker_address = 'broker.hivemq.com'
port = 1883
client_id = f'python-mqtt-{random.randint(0, 100)}'


client = mqttclient.Client(client_id)
client.on_connect = on_connect
client.connect(broker_address, port)
client.loop_start()

client.subscribe("praan/mqtt")
while True:
    time.sleep(1)
    client.on_message = on_message

# client.loop_end()