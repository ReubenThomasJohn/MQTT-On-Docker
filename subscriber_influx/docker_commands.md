```docker build --tag subscriber-influx  .```

```docker run -it -p 8001:81 -e INFLUX_API_TOKEN='qO_163duBYgSwwLeNko6AFA1EIVhNSHGJLPEgJqvIig6csGzRVgTzGOyUtB7ylQFEFDqb2O8r2A7cXfqChDd3Q=='  subscriber-influx```