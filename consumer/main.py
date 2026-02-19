from redis_connection import get_redis_connection
import json 

REDIS_CONNECTION = get_redis_connection()

while True:
    # Blocking pop to wait for new messages
    urgent = REDIS_CONNECTION.brpop('URGENT')
    normal = REDIS_CONNECTION.brpop('NORMAL')
    
    urgent_info = json.loads(urgent[1].decode('utf-8'))
    normal_info = json.loads(normal[1].decode('utf-8'))

    # Retrieve full message details from Redis
    full_urgent = REDIS_CONNECTION.hgetall(f"message:{urgent['URGENT']}")
    full_normal = REDIS_CONNECTION.hgetall(f"message:{normal['NORMAL']}")



 