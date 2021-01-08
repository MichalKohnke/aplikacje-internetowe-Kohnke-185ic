from redis import Redis

redis_connection = Redis(decode_responses=True) #po³¹czenie

key ="some-key" #klucz
value ="some-val" #wartoœæ

redis_connection.set(key, value) 
print(redis_connection.get(key)) #odczytanie wartoœci

redis_connection.append(key,"-append") #do³¹czenie stringa do wartoœci
print(redis_connection.get(key))

redis_connection.delete(key) #usuniêcie klucza
print(redis_connection.get(key))