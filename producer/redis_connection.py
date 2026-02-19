from redis import Redis

REDIS_HOST: str = 'localhost'

def get_redis_connection():
    return Redis(host=REDIS_HOST, port=6379, decode_responses=True)

