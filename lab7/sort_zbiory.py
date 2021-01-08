from redis import Redis

redis_connection = Redis(decode_responses=True)

redis_connection.zadd("sorted_set_key",{"key1": 5})  #wariacja zbiorów - posortowany zbiór(sorted set), ka¿dy element zbioru ma pewn¹ wartoœæ zwan¹ score(mo¿na okreœliæ to "wag¹"), s³u¿¹c¹ do zachowania kolejnoœci
redis_connection.zadd("sorted_set_key",{"key2": 2}) #komenda ZADD dodajey elementy
redis_connection.zadd("sorted_set_key",{"key3": 6})
redis_connection.zadd("sorted_set_key",{"key4": 10})

print(redis_connection.zrange("sorted_set_key",0, -1)) #ZRANGE pobiera elementy