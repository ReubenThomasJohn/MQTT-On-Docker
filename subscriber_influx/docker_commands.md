```docker build --tag subscriber-influx  .```

```docker run -it -p 8001:81 -e INFLUX_API_TOKEN=<influx_api_token>  subscriber-influx```