import influxdb_client, os
from influxdb_client import BucketsApi
from influxdb_client.client.write_api import SYNCHRONOUS
import paho.mqtt.client as mqttclient
import datetime

import random
import time
# from dotenv import load_dotenv
# load_dotenv()

token = os.environ.get("INFLUX_API_TOKEN") # environment vars
# token = os.getenv("INFLUX_API_TOKEN")
org = "Dev"
url = "https://ap-southeast-2-1.aws.cloud2.influxdata.com"

bucket_name="SensorDB1"

influx_client = influxdb_client.InfluxDBClient(url=url, token=token, org=org)

try:
  # bucket exists
  print(BucketsApi(influx_client).find_bucket_by_name(bucket_name))
except:
  # create bucket if it doesn't exist
  bucket = BucketsApi(influx_client).create_bucket(bucket_name=bucket_name)

def on_connect(client, userdata, flags, rc):
    if rc==0:
        print("client is connected")
        global connected
        connected=True
    else:
        print("client is not connected")

def on_message(client, userdata, message):
  write_api = influx_client.write_api(write_options=SYNCHRONOUS)
  time.sleep(.1)
  try:
      read_message = message.payload.decode("utf-8")
      frames = read_message[1:-1].split(',')
      for frame in frames:
        arr = frame.split()  
        # time_string = str(arr[1]) + " " + str(arr[2])
        # time_stamp = convert_to_nanoseconds(time_string)      
        a = {'device': arr[0][1:], 'wind_speed':float(arr[3]), 
        'wind_heading': float(arr[4]), 'pm1':float(arr[5]), 'pm25':float(arr[6]), 'pm10':float(arr[7][:-1])}
        # print(str(arr[1]) + " " + str(arr[2])) #this is the "_id" field in mongo doc   
        JsonData = {"measurement":"SensorA1-MQTT",
            "tags": {
              "sensor_id": "123",              
            },
            "fields": a
            # "time" : time_stamp
            } 
        print(JsonData)
        write_api.write(bucket=bucket_name, record=JsonData)
        

      print("Topic: " + str(message.topic))
  
  except:
      pass

def convert_to_nanoseconds(time_string):
    converted = datetime(int(time_string[:4]), int(time_string[6]), 
            int(time_string[8:10]), int(time_string[11:13]),
            int(time_string[14:16]), int(time_string[17:19])).timestamp()
    return converted


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
    client.on_message = on_message
    # time.sleep(5)

