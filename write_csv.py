#!/usr/bin/env python3
import random
import pandas as pd
import datetime
import time
counter = 1

now = time.time()

while True:
    trigger = time.time() - now
    while not trigger < 10:
        # message accumulation due to the network being down
        while counter < random.randint(0, 15):
            df = pd.DataFrame({'device':str('abc123'), 't':datetime.datetime.now(), 'w':1.23, 'h':23, 
            'pm1': 12, 'pm25': 45, 'pm10':56}, index=[counter]) 
            # df.index = np.arange(1, len(df) + 1)
            df.to_csv('praan_sample.csv', mode='a', header=False)
            time.sleep(3)
            counter += 1
        trigger = 0
        counter = 1
        now = time.time()
    else:
        df = pd.DataFrame({'device':str('abc123'), 't': datetime.datetime.now(), 'w':1.23, 'h':23,
        'pm1': 12, 'pm25': 45, 'pm10':56}, index=[1])
        # df.index = np.arange(1, len(df) + 1)
        df.to_csv('praan_sample.csv', header=True)
        time.sleep(3)