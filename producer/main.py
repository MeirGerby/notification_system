# import os 
import json
from typing import List

from priority_logic import ReadData, Data, Priority
from redis_connection import get_redis_connection

# PATH = os.getenv('PATH', r'data\border_alerts.json') 
PATH = r'data\border_alerts.json'
REDIS_CONNECTION = get_redis_connection()
def main():
    data = ReadData() 
    notifications: list = data.get_notification_data(PATH)
    notifications_list: List[Data] = []
    for n in notifications:
        notification = Data(**n)
        notifications_list.append(notification)
    proiriry = Priority(notifications_list)
    for p in proiriry:
        REDIS_CONNECTION.set(p.priority ,json.dumps(p)) # type: ignore
    return notifications

if __name__ == "__main__":
    main()