from redis import Redis

redis_connection = Redis(decode_responses=True)

list_key ="example-list" #klucz

redis_connection.rpush(list_key,1,2,3,4,5) #dodanie element�w do listy z prawej strony, RPUSH

print(redis_connection.lrange(list_key,0, -1)) #pobranie warto�ci z listy dzi�ki LRANGE, kt�re pobiera warto�ci od indeksu 0 do -1, czyli do ko�ca

print(redis_connection.lrange(list_key,1,3)) #LRANGE z innymi indeksami