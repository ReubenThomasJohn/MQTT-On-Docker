from mqtt_device import MQTT_Device
from time import sleep

sensor = MQTT_Device('s02')
print(sensor)

sensor.connect_broker('broker.hivemq.com', 1883, 'praan/mqtt')
sensor.loop_start()
while True:
    data = sensor.read_from_storage('praan_sample.csv')
    sensor.publish_to_topic(data, sensor.topic)
    sleep(2)