<<<<<<< HEAD
from redis import Redis

redis_connection = Redis(decode_responses=True) #po��czenie

key ="some-key" #klucz
value ="some-val" #warto��

redis_connection.set(key, value) 
print(redis_connection.get(key)) #odczytanie warto�ci

redis_connection.append(key,"-append") #do��czenie stringa do warto�ci
print(redis_connection.get(key))

redis_connection.delete(key) #usuni�cie klucza
=======
from redis import Redis

redis_connection = Redis(decode_responses=True) #po��czenie

key ="some-key" #klucz
value ="some-val" #warto��

redis_connection.set(key, value) 
print(redis_connection.get(key)) #odczytanie warto�ci

redis_connection.append(key,"-append") #do��czenie stringa do warto�ci
print(redis_connection.get(key))

redis_connection.delete(key) #usuni�cie klucza
>>>>>>> 3c03acf3ac812a0ae56de0c38ea26bf8bc95dc55
print(redis_connection.get(key))