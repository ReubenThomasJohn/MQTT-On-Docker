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
        
        def on_connect(self, client, userdata, flags, rc):
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
    
    def push_to_broker(self, sleep_time = 5):
        self = self.connect_broker('broker.hivemq.com', 1883, 'praan/mqtt')
        self.loop_start()
        while True:
            data = self.read_from_storage('praan_sample.csv')
            self.publish_to_topic(data, self.topic)
            sleep(sleep_time)

    def receive_from_broker(self, sleep_time = 5):
        pass

sensor = MQTT_Device('s02')
print(sensor)
sensor.loop()
    