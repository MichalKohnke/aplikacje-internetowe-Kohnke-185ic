<<<<<<< HEAD
from redis import Redis

redis_connection = Redis(decode_responses=True, db=0)

stream_name ='testowy_strumien'

redis_connection.xadd(stream_name,{'testowy_klucz': 'testowa_wartosc'}) #dodanie do strumienia s�ownika 
message = redis_connection.xread({stream_name: '0-0'}, block=None, count=1) #odczytanie ze strumienia podan� w parametrze 'count' ilo�� element�w; 'block' - okre�la czy i je�li tak, to na ile ms, funcka ta ma by� blokuj�ca
=======
from redis import Redis

redis_connection = Redis(decode_responses=True, db=0)

stream_name ='testowy_strumien'

redis_connection.xadd(stream_name,{'testowy_klucz': 'testowa_wartosc'}) #dodanie do strumienia s�ownika 
message = redis_connection.xread({stream_name: '0-0'}, block=None, count=1) #odczytanie ze strumienia podan� w parametrze 'count' ilo�� element�w; 'block' - okre�la czy i je�li tak, to na ile ms, funcka ta ma by� blokuj�ca
>>>>>>> 3c03acf3ac812a0ae56de0c38ea26bf8bc95dc55
print(message)