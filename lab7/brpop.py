<<<<<<< HEAD
from redis import Redis

redis_connection = Redis(decode_responses=True)

list_key ="example-list"

while True: 
    print(redis_connection.brpop(list_key)) #BRPOP blokuje program, je�li w li�cie nie ma element�w, za� gdy s�, pobiera elementy od prawej strony i po ostatnim blokuje program
=======
from redis import Redis

redis_connection = Redis(decode_responses=True)

list_key ="example-list"

while True: 
    print(redis_connection.brpop(list_key)) #BRPOP blokuje program, je�li w li�cie nie ma element�w, za� gdy s�, pobiera elementy od prawej strony i po ostatnim blokuje program
>>>>>>> 3c03acf3ac812a0ae56de0c38ea26bf8bc95dc55
    