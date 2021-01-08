from redis import Redis
from time import sleep
from datetime import datetime

redis_connection = Redis(decode_responses=True)

redis_connection.setex("key",30,"value") #wartoœæ 'value' pod kluczem 'key' i ustawione 30s jako TTL przy u¿yciu komendy SETEX

#redis_connection.set("key","value")
#redis_connection.expire("key",30) MO¯NA ZROBIÆ TE¯ W TEN SPOSÓB; SETEX - SET i EXPIRE

print(datetime.now().time(), redis_connection.get("key")) #od razu odczytujemy - nie ma problemu
sleep(10) #10sekund odczekania
print(datetime.now().time(), redis_connection.get("key")) #tu dalej dostêpna wartoœæ
sleep(30) #30 sekund odczekania, po czasie ju¿
print(datetime.now().time(), redis_connection.get("key")) #NONE, poniewa¿ czas od momentu zapisu wartoœci jest wiêkszy ni¿ ustawione wczeœniej 30sekund