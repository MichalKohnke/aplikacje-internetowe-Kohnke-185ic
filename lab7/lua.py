from redis import Redis

redis_connection = Redis(decode_responses=True, db=0)


script ="""
return {KEYS[1],KEYS[2],ARGV[1],ARGV[2]}
""" #skrypt Lua

print(redis_connection.eval(script,2,1,2,'first','second')) #komenda EVAL, wykorzystana aby przekazaæ w niej skrypt LUA, Redis odbiera ten kod, wykonuje go i zwraca rezultat; drugi parametr to iloœæ argumentów, które przeka¿emy do funkcji