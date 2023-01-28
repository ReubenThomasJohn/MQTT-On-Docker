```docker build --tag subscriber-mongo .```

```docker run -it -p 8000:80 -e MONGO_CONNECTION_STRING='mongodb+srv://admin-reuben:test123@todo-list-cluster.iguuebo.mongodb.net/?retryWrites=true&w=majority' subscriber-mongo```