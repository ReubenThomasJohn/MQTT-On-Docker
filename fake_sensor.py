#!/usr/bin/env python3
from paho.mqtt import client as mqtt_client
import random
from time import sleep
import pandas as pd

def read_from_csv(csv_file_path):
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

broker = 'broker.hivemq.com'
port = 1883
topic = "praan/mqtt"
# generate client ID with pub prefix randomly
client_id = f'python-mqtt-{random.randint(0, 100)}'

client = None

def connect_mqtt():
    global username, password
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)
    # client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client

def publish(client, data):
    msg = str(data)
    result = client.publish(topic, msg)
    # result: [0, 1]
    status = result[0]
    if status == 0:
        print(f"Sent `{msg}` to topic `{topic}`")
    else:
        print(f"Failed to send message to topic {topic}")

client = connect_mqtt()
client.loop_start()
while True:
    data = read_from_csv('praan_sample.csv')
    publish(client, data)
    sleep(5)

    
