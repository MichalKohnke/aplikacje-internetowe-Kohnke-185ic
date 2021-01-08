from redis import Redis

redis_connection = Redis(decode_responses=True)

hash_key ='test_hash' #stworzenie pod kluczem "test_hash" s�ownika(tablica asocjacyjna)

redis_connection.hset(hash_key,'key','value') #jeden klucz "key" o warto�ci "value", dodanie elementu HSET
redis_connection.hgetall()