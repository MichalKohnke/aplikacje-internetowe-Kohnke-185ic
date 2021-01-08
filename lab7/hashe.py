<<<<<<< HEAD
from redis import Redis

redis_connection = Redis(decode_responses=True)

hash_key ='test_hash' #stworzenie pod kluczem "test_hash" s³ownika(tablica asocjacyjna)

redis_connection.hset(hash_key,'key','value') #jeden klucz "key" o wartoœci "value", dodanie elementu HSET
=======
from redis import Redis

redis_connection = Redis(decode_responses=True)

hash_key ='test_hash' #stworzenie pod kluczem "test_hash" s³ownika(tablica asocjacyjna)

redis_connection.hset(hash_key,'key','value') #jeden klucz "key" o wartoœci "value", dodanie elementu HSET
>>>>>>> 3c03acf3ac812a0ae56de0c38ea26bf8bc95dc55
redis_connection.hgetall()