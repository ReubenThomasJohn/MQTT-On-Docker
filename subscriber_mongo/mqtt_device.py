#!/usr/bin/env python3
from paho.mqtt import client as mqtt_client
import random
from time import sleep
import pandas as pd

# client_id = f'python-mqtt-{random.randint(0, 100)}'

class MQTT_Device(mqtt_client.Client):
    def __init__(self, client_id):
        super().__init__(client_id)
        print(self)

    def connect_broker(self, broker, port, topic):
        global username, password
        self.topic = topic
        
        def on_connect(self, userdata, flags, rc):
            if rc == 0:
                print("Connected to MQTT Broker!")
            else:
                print("Failed to connect, return code %d\n", rc)

        self.on_connect = on_connect
        self.connect(broker, port)
        return self

    def publish_to_topic(self, data, topic):
        msg = str(data)
        result = self.publish(topic, msg)
        # result: [0, 1]
        status = result[0]
        if status == 0:
            print(f"Sent `{msg}` to topic `{topic}`")
        else:
            print(f"Failed to send message to topic {topic}")

    def read_from_storage(self, csv_file_path):
        df = pd.read_csv(csv_file_path) #optimize this part
        # print(len(df))
        data = []
        for i in range(len(df)):

            sensor_id = df['device'][i]
            timestamp = df['t'][i]
            wind_speed = df['w'][i]
            wind_heading = df['h'][i]
            pm1 = df['pm1'][i]
            pm25 = df['pm25'][i]
            pm10 = df['pm10'][i]

            data_string = str(sensor_id) + " " + str(timestamp) + " " + str(wind_speed) + " " + str(wind_heading) \
            + " " + str(pm1) + " " + str(pm25) + " " + str(pm10)

            data.append(data_string)
        return data

    def add_collection(self, collection):
        self.collection = collection

    def on_message(self, client, userdata, message):
        global collection
        print(collection)
        try:
            read_message = message.payload.decode("utf-8")
            frames = read_message[1:-1].split(',')
            # print(frames)
            data_to_DB = []
            for index, frame in enumerate(frames):
                arr = frame.split()        
                a = {'device': arr[0][1:], 'wind_speed':arr[3], # add '_id': str(arr[1]) + " " + str(arr[2])
                'wind_heading': arr[4], 'pm1':arr[5], 'pm25':arr[6], 'pm10':arr[7][:-1]}
                data_to_DB.append(a)
                # print(str(arr[1]) + " " + str(arr[2])) #this is the "_id" field in mongo doc
            
            print(data_to_DB) 
            collection.insert_many(data_to_DB) 
            print("Topic: " + str(message.topic))
        
        except:
            pass

    # def push_to_broker(self, sleep_time = 5):
    #     self = self.connect_broker('broker.hivemq.com', 1883, 'praan/mqtt')
    #     self.loop_start()
    #     while True:
    #         data = self.read_from_storage('praan_sample.csv')
    #         self.publish_to_topic(data, self.topic)
    #         sleep(sleep_time)
    

    