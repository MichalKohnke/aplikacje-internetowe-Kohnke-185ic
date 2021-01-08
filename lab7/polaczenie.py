from redis import Redis
redis_connection = Redis(decode_responses=True)
print(redis_connection.ping())