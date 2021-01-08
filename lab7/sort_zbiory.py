from redis import Redis

redis_connection = Redis(decode_responses=True)

redis_connection.zadd("sorted_set_key",{"key1": 5})  #wariacja zbior�w - posortowany zbi�r(sorted set), ka�dy element zbioru ma pewn� warto�� zwan� score(mo�na okre�li� to "wag�"), s�u��c� do zachowania kolejno�ci
redis_connection.zadd("sorted_set_key",{"key2": 2}) #komenda ZADD dodajey elementy
redis_connection.zadd("sorted_set_key",{"key3": 6})
redis_connection.zadd("sorted_set_key",{"key4": 10})

print(redis_connection.zrange("sorted_set_key",0, -1)) #ZRANGE pobiera elementy