import influxdb_client, os
from influxdb_client import BucketsApi, Point
from influxdb_client.client.write_api import SYNCHRONOUS
import paho.mqtt.client as mqttclient
import datetime
from datetime import timezone
import pytz

import random
import time
from dotenv import load_dotenv
load_dotenv()

# token = os.environ.get("INFLUX_API_TOKEN") # environment vars
token = os.getenv("INFLUX_API_TOKEN")
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

def convert_to_nanoseconds(time_string):
    converted = datetime.datetime(int(time_string[:4]), int(time_string[6]), 
            int(time_string[8:10]), int(time_string[11:13]),
            int(time_string[14:16]), int(time_string[17:19]), int(time_string[20:]))
    converted = converted.replace(tzinfo=timezone.utc)
    return converted

def on_message(client, userdata, message):
  write_api = influx_client.write_api(write_options=SYNCHRONOUS)
  time.sleep(.1)
  read_message = message.payload.decode("utf-8")
  if read_message[0] == '[':
    frames = read_message[1:-1].split(',')
  else:
    frames = read_message.split(',')
  # print("First: ", frames[0])
  for frame in frames:
    arr = frame.split() 
    # print(arr)   
    # # print(arr)
    # 'a1 2023-01-29 18:47:29.870494 34 198 50 42 50'
    # a= {'device': arr[0],
    # 'wind_speed':float(arr[3]),
    # 'wind_heading': float(arr[4]),
    # 'pm1':float(arr[5]),
    # 'pm25':float(arr[6]),
    # 'pm10':float(arr[7])}

    # # print(str(arr[1]) + " " + str(arr[2])) #this is the "_id" field in mongo doc   
    # JsonData = {"measurement":"SensorA1-MQTT",
    #     "tags": {
    #       "sensor_id": "123",              
    #     },
    #     "fields": a
    #     # "time" : time_stamp
    #     } 
    # print(JsonData)

    
    time_string = str(arr[1]) + " " + str(arr[2])
    # print("Time String: ", time_string)
    # time_stamp = convert_to_nanoseconds(time_string) 
    
    
    # try:
    #   print("Time stamp: ", time_stamp)
    #   print()
    #   print("UTC Now: ", datetime.datetime.utcnow())
    # except:
    #   print("excepted")

    local = pytz.timezone("Asia/Kolkata")
    naive = datetime.datetime.strptime(time_string, "%Y-%m-%d %H:%M:%S.%f")
    local_dt = local.localize(naive, is_dst=True)
    utc_dt = local_dt.astimezone(pytz.utc)
    influx_timestamp = utc_dt.strftime("%Y-%m-%d %H:%M:%S.%f")

    point = Point("measurement") \
    .field('sensor_id', arr[0]) \
    .field('wind_speed', float(arr[3])) \
    .field('wind_heading', float(arr[4])) \
    .field('pm1', float(arr[5])) \
    .field('pm25', float(arr[6])) \
    .field('pm10', float(arr[7]))\
    .time(time=influx_timestamp)     #.time(time=datetime.datetime.utcnow()) \
    print(f'Writing to InfluxDB cloud: {point.to_line_protocol()} ...')
    # write_api.write(bucket=bucket_name, org=org, record=JsonData)

    print()
    print('success')
    print()

    write_api.write(bucket=bucket_name, record=point)
    # write_api.write(bucket=bucket_name, record=JsonData)
      

    print("Topic: " + str(message.topic))

  # except:
  #   print('excepted')
  #     # pass




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

