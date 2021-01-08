from redis import Redis

redis_connection = Redis(decode_responses=True)

list_key ="example-list"

while True: 
    print(redis_connection.brpop(list_key)) #BRPOP blokuje program, jeœli w liœcie nie ma elementów, zaœ gdy s¹, pobiera elementy od prawej strony i po ostatnim blokuje program
    