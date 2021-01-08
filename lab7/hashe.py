from redis import Redis

redis_connection = Redis(decode_responses=True)

hash_key ='test_hash' #stworzenie pod kluczem "test_hash" s³ownika(tablica asocjacyjna)

redis_connection.hset(hash_key,'key','value') #jeden klucz "key" o wartoœci "value", dodanie elementu HSET
redis_connection.hgetall()