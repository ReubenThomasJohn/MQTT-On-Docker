'''
function that will pull data from the csv, and turn it into a JSON object
'''

'''
TODO:
With the csv file attached, build a basic transmission system to replicate the device sending packets with the above data using any free
MQTT.
Send data in timestamped(as per csv) packets as well as a packet containing multiple frames stacked (replicating no network cases
and data being accumulated over time and being sent when the network is up).

NOTES:
0. Add around 10 rows in the excel
1. Get the full MQTT setup working now locally
2. dockerize and check if it's working locally
3. Deploy container on ECS and check if its working
4. Ask for CSV, and you can write a fakeData function that every 2 mins keeps adding rows to CSV and removing the previous rows,
only 2 rows must be there in the CSV
5. Every 5 mins, network down occurs need to check whether csv needs to get stacked or
something in the function. 
'''

import pandas as pd

def sensor_send(csv_file_path):
    df = pd.read_csv(csv_file_path) # can use nrows = 

    return df['t'].to_string()

# print(sensor_send('praan_sample.csv'))

