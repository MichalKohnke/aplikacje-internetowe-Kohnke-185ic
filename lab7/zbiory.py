<<<<<<< HEAD
from redis import Redis

redis_connection = Redis(decode_responses=True)

redis_connection.sadd("key","val1")
redis_connection.sadd("key","val2")
redis_connection.sadd("key","val3") #SADD - dodaje element do zbioru

=======
from redis import Redis

redis_connection = Redis(decode_responses=True)

redis_connection.sadd("key","val1")
redis_connection.sadd("key","val2")
redis_connection.sadd("key","val3") #SADD - dodaje element do zbioru

>>>>>>> 3c03acf3ac812a0ae56de0c38ea26bf8bc95dc55
print(redis_connection.smembers("key")) #SMEMBERS - pobiera elementy