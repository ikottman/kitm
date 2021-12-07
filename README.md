# Kottman in the Middle

simple proxy for logging requests, including response bodies

# How to Use

1. Configure the `PORT` with the service you want to proxy to in [docker-compose.yml](https://github.com/ikottman/kitm/blob/main/docker-compose.yml#L8)
2. start the proxy `docker-compose up`
3. Call the proxy instead of your service, at `localhost:8000`
4. Requests and responses are logged to `./logs/log.json`
