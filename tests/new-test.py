import pandas as pd

def read_from_csv(csv_file_path):
    df = pd.read_csv(csv_file_path) #optimize this part
    print(len(df))
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

print(read_from_csv('praan_sample.csv'))