<<<<<<< HEAD
from redis import Redis
redis_connection = Redis(decode_responses=True)
=======
from redis import Redis
redis_connection = Redis(decode_responses=True)
>>>>>>> 3c03acf3ac812a0ae56de0c38ea26bf8bc95dc55
print(redis_connection.ping())