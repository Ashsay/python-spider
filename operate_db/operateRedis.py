from redis import StrictRedis

redis = StrictRedis(host='localhost',port=6379,db=0,password='root')
redis.set('name','Ashsay')
print(redis.get('name'))