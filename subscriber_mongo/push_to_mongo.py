import paho.mqtt.client as mqttclient
import time
import random
from pymongo import MongoClient
import os

import os
# from dotenv import load_dotenv
# load_dotenv()
connection_string = os.environ.get("MONGO_CONNECTION_STRING") # environment vars

# 50 per frame

def on_connect(client, userdata, flags, rc):
    if rc==0:
        print("client is connected")
        global connected
        connected=True
    else:
        print("client is not connected")

def on_message(client, userdata, message):

    try:
        read_message = message.payload.decode("utf-8")
        frames = read_message[1:-1].split(',')
        # print(frames)
        data_to_DB = []
        for index, frame in enumerate(frames):
            arr = frame.split()        
            a = {'device': arr[0][1:], 'wind_speed':arr[3], '_id': str(arr[1]) + " " + str(arr[2]),
            'wind_heading': arr[4], 'pm1':arr[5], 'pm25':arr[6], 'pm10':arr[7][:-1]}
            data_to_DB.append(a)
            # print(str(arr[1]) + " " + str(arr[2])) #this is the "_id" field in mongo doc
        
        print(data_to_DB)   
        collection.insert_many(data_to_DB) 
        print("Topic: " + str(message.topic))
    
    except:
        pass


# Set up client for MongoDB
# mongoClient=MongoClient("mongodb://localhost:27017/")
# connection_string = os.getenv('MONGO_CONNECTION_STRING')
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