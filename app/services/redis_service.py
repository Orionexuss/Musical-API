from redis import Redis

class RedisService:
    def __init__(self, host='localhost', port=6379, db=0):
        self.redis = Redis(host=host, port=port, db=db, decode_responses=True)
    
    def set_value(self, key: str, value: str):
        self.redis.set(key, value)
        
    def get_value(self, key: str):
        print(f'this is the key: {key}')
        return self.redis.get(key)
        
    def del_value(self, key:str):
        self.redis.delete(key)
        