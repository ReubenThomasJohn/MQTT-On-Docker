```docker build --tag subscriber-mongo .```

```docker run -it -p 8000:80 -e MONGO_CONNECTION_STRING=<mongo_connection_string> subscriber-mongo```