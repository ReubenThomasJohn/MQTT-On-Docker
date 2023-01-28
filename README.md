TODO:
~~1. Fix influxDB pusher~~ \
~~2. Write ```MQTT_Device()``` class that inherits the paho.mqtt() class~~ \
3. Base publishers and subscribers on top of that \
4. Put the publisher and two subscribers on AWS \
5. Create better sim data function \
6. http://www.steves-internet-guide.com/client-connections-python-mqtt/#:~:text=The%20Paho%20client%20provides%20the,you%20will%20need%20to%20examine. : Check to see if disconnection sim can be improved.

NOW:
1. Better sim data, bring write csv inside publisher
2. Git push
3. Put everything on ec2
4. Fill install_docker_ec2.md file

```loop_start()``` handles reconnections gracefully.,

times are saved in utc


FOR LATER:
1. Docker compose file for running everything in containers locally
2. Terraform files for automating infra creation
3. Wrap everything in Github Actions