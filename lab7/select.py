<<<<<<< HEAD
from redis import Redis

redis_connection = Redis(decode_responses=True) #pierwsze po��czenie(przestrze�)

redis_connection.set("key","value") #przypisanie warto�ci

redis_connection_1 = Redis(decode_responses=True, db=1) #drugie po��czenie(przestrze�, wybrana 1)

print(redis_connection_1.get("key")) #odczytanie warto�ci, NONE, poniewa� przypisana wy�ej warto�� zosta�a zapisana na bazie zerowej, a odczytujemy tutaj z bazy pierwszej

=======
from redis import Redis

redis_connection = Redis(decode_responses=True) #pierwsze po��czenie(przestrze�)

redis_connection.set("key","value") #przypisanie warto�ci

redis_connection_1 = Redis(decode_responses=True, db=1) #drugie po��czenie(przestrze�, wybrana 1)

print(redis_connection_1.get("key")) #odczytanie warto�ci, NONE, poniewa� przypisana wy�ej warto�� zosta�a zapisana na bazie zerowej, a odczytujemy tutaj z bazy pierwszej

>>>>>>> 3c03acf3ac812a0ae56de0c38ea26bf8bc95dc55
print(redis_connection.get("key")) #odczytanie warto�ci z bazy zerowej