<<<<<<< HEAD
from redis import Redis

redis_connection = Redis(decode_responses=True)

key ="some-key"
value =55

redis_connection.set(key, value) 
print(redis_connection.get(key)) #odczytanie warto�ci

print(redis_connection.incr(key,5)) #zwi�kszenie warto�ci, increment

=======
from redis import Redis

redis_connection = Redis(decode_responses=True)

key ="some-key"
value =55

redis_connection.set(key, value) 
print(redis_connection.get(key)) #odczytanie warto�ci

print(redis_connection.incr(key,5)) #zwi�kszenie warto�ci, increment

>>>>>>> 3c03acf3ac812a0ae56de0c38ea26bf8bc95dc55
print(redis_connection.decr(key,20)) #zmniejsze warto�ci, decrement