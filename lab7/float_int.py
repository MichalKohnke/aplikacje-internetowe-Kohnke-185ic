from redis import Redis

redis_connection = Redis(decode_responses=True)

key ="some-key"
value =55

redis_connection.set(key, value) 
print(redis_connection.get(key)) #odczytanie wartoœci

print(redis_connection.incr(key,5)) #zwiêkszenie wartoœci, increment

print(redis_connection.decr(key,20)) #zmniejsze wartoœci, decrement