<<<<<<< HEAD
from redis import Redis

redis_connection = Redis(decode_responses=True, db=0)


script ="""
return {KEYS[1],KEYS[2],ARGV[1],ARGV[2]}
""" #skrypt Lua

=======
from redis import Redis

redis_connection = Redis(decode_responses=True, db=0)


script ="""
return {KEYS[1],KEYS[2],ARGV[1],ARGV[2]}
""" #skrypt Lua

>>>>>>> 3c03acf3ac812a0ae56de0c38ea26bf8bc95dc55
print(redis_connection.eval(script,2,1,2,'first','second')) #komenda EVAL, wykorzystana aby przekaza� w niej skrypt LUA, Redis odbiera ten kod, wykonuje go i zwraca rezultat; drugi parametr to ilo�� argument�w, kt�re przeka�emy do funkcji