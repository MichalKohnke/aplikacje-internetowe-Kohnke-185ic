from redis import Redis

redis_connection = Redis(decode_responses=True)

redis_connection.sadd("key","val1")
redis_connection.sadd("key","val2")
redis_connection.sadd("key","val3") #SADD - dodaje element do zbioru

print(redis_connection.smembers("key")) #SMEMBERS - pobiera elementy