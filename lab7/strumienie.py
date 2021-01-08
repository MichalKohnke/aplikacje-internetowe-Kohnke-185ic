from redis import Redis

redis_connection = Redis(decode_responses=True, db=0)

stream_name ='testowy_strumien'

redis_connection.xadd(stream_name,{'testowy_klucz': 'testowa_wartosc'}) #dodanie do strumienia s³ownika 
message = redis_connection.xread({stream_name: '0-0'}, block=None, count=1) #odczytanie ze strumienia podan¹ w parametrze 'count' iloœæ elementów; 'block' - okreœla czy i jeœli tak, to na ile ms, funcka ta ma byæ blokuj¹ca
print(message)