from redis import Redis

redis_connection = Redis(decode_responses=True) #pierwsze po³¹czenie(przestrzeñ)

redis_connection.set("key","value") #przypisanie wartoœci

redis_connection_1 = Redis(decode_responses=True, db=1) #drugie po³¹czenie(przestrzeñ, wybrana 1)

print(redis_connection_1.get("key")) #odczytanie wartoœci, NONE, poniewa¿ przypisana wy¿ej wartoœæ zosta³a zapisana na bazie zerowej, a odczytujemy tutaj z bazy pierwszej

print(redis_connection.get("key")) #odczytanie wartoœci z bazy zerowej