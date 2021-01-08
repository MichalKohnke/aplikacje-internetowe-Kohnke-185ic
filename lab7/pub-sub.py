<<<<<<< HEAD
from redis import Redis

redis_connection = Redis(decode_responses=True)

pubsub = redis_connection.pubsub()
pubsub.subscribe("testowa_kanal_komunikacyjny") #subskrybent; klucz o nazwie "testowa_kanal_komunikacyjny

for message in pubsub.listen():
=======
from redis import Redis

redis_connection = Redis(decode_responses=True)

pubsub = redis_connection.pubsub()
pubsub.subscribe("testowa_kanal_komunikacyjny") #subskrybent; klucz o nazwie "testowa_kanal_komunikacyjny

for message in pubsub.listen():
>>>>>>> 3c03acf3ac812a0ae56de0c38ea26bf8bc95dc55
    print(message)