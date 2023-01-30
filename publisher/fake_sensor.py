#!/usr/bin/env python3
from paho.mqtt import client as mqtt_client
import random
import time
import pandas as pd
import datetime
import threading
import sys
import os

# def write_csv():
#     counter = 1
#     now = time.time()

#     while True:
#         trigger = time.time() - now
#         while not trigger < 10:
#             # message accumulation due to the network being down
#             while counter < random.randint(0, ):
#                 df = pd.DataFrame({'device':str('abc123'), 't':datetime.datetime.now(), 'w':1.23, 'h':23, 
#                 'pm1': 12, 'pm25': 45, 'pm10':56}, index=[counter]) 
#                 # df.index = np.arange(1, len(df) + 1)
#                 df.to_csv('praan_sample.csv', mode='a', header=False)
#                 time.sleep(10)
#                 counter += 1
#             trigger = 0
#             counter = 1
#             now = time.time()
#         else:
#             df = pd.DataFrame({'device':str('abc123'), 't': datetime.datetime.now(), 'w':1.23, 'h':23,
#             'pm1': 12, 'pm25': 45, 'pm10':56}, index=[1])
#             # df.index = np.arange(1, len(df) + 1)
#             df.to_csv('praan_sample.csv', mode = 'a', header=True)
#             time.sleep(10)

# def save_to_storage(filename='praan_sample.csv'):
#     network_downtime = random.randint(20, 40)
#     print("Network down for: ", str(network_downtime) + " s")
#     curr_time = time.time()
#     while True:
#         if time.time() - curr_time < network_downtime:
#             df = pd.DataFrame({'device':str('a'), 't':datetime.datetime.now(), 'w':random.randint(32, 36), 
#             'h':random.randint(180, 200), 'pm1': random.randint(40, 50), 
#             'pm25': random.randint(40, 80), 'pm10': random.randint(50, 90)}, index=[0]) #index = [counter] 
#             # df.index = np.arange(1, len(df) + 1)
#             with open(filename, 'a') as f:
#                 # df.to_csv('praan_sample.csv', mode='a', header=False)
#                 df.to_csv(f, mode='a', header=f.tell()==0)
#                 time.sleep(5) # sensor senses every 5 seconds
#         else:
#             sys.exit()

def save_to_storage(filename='praan_sample.csv'):
    network_downtime = random.randint(20, 40)
    print("Network down for: ", str(network_downtime) + " s")
    curr_time = time.time()
    while time.time() - curr_time < network_downtime:

        df = pd.DataFrame({'device':str('a'), 't':datetime.datetime.now(), 'w':random.randint(32, 36), 
        'h':random.randint(180, 200), 'pm1': random.randint(40, 50), 
        'pm25': random.randint(40, 80), 'pm10': random.randint(50, 90)}, index=[0]) #index = [counter] 
        # df.index = np.arange(1, len(df) + 1)
        with open(filename, 'a') as f:
            # df.to_csv('praan_sample.csv', mode='a', header=False)
            df.to_csv(f, mode='a', header=f.tell()==0)
            time.sleep(5) # sensor senses every 5 seconds
    else:
        sys.exit()

def read_from_storage(csv_file_path):
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
        + " " + str(pm1) + " " + str(pm25) + " " + str(pm10) + " " + str("end")

        print(timestamp)

        # data_string = sensor_id + " " + timestamp + " " + wind_speed + " " + wind_heading \
        # + " " + pm1 + " " + pm25 + " " + pm10

        
        data.append(data_string)
        # ["['a", '2023-01-30', '10:48:58.436465', '35', '185', '49', '69', "50'"]
    # print('Data: ', data)
    return data

def generate_values():
    sensor_id = 'a'
    timestamp = datetime.datetime.now()
    wind_speed = random.randint(32, 36)
    wind_heading = random.randint(180, 200)
    pm1 = random.randint(40, 50) #micro-gram/m^3
    pm25 = random.randint(40, 80)
    pm10 = random.randint(50, 90)

    data = str(sensor_id) + " " + str(timestamp) + " " + str(wind_speed) + " " + str(wind_heading) \
        + " " + str(pm1) + " " + str(pm25) + " " + str(pm10)
    
    print(timestamp)
    time.sleep(5)
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
    # time.sleep(5)
    # result: [0, 1]
    status = result[0]
    if status == 0:
        print(f"Sent `{msg}` to topic `{topic}`")
    else:
        print(f"Failed to send message to topic {topic}")




client = connect_mqtt()
client.loop_start()
# os.remove('praan_sample.csv')

while True:
    network_down = 4 == random.randint(1, 5)
    print(network_down)
    if network_down:
        t1 = threading.Thread(target=save_to_storage)
        t1.start()
        t1.join()
        data = read_from_storage('praan_sample.csv')
        publish(client, data)
        # print("Stored data: ", data)
        os.remove('praan_sample.csv')
        print("storage cleared \n")
        # time.sleep(2)
    else:
        data = generate_values() 
        publish(client, data)
        # time.sleep(2)


# https://www.mdpi.com/2073-4433/6/1/150

    
