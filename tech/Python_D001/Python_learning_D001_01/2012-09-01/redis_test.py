import sys
# print sys.path

sys.path.append("/home/allen/Tools/Python_workspace/py_3th_model/redis-py")
# example
# >>> sys.path.append("/home/allen/Tools/Python_workspace/py_3th_model/redis-py")
# print sys.path
import redis

r = redis.StrictRedis(host='127.0.0.1', port=6379)  
r.set('foo', 'hello')  
r.rpush('mylist', 'one')  

print r.get('foo')  
print r.rpop('mylist') 