# import os 

from priority_logic import ReadData, Data

# PATH = os.getenv('PATH', r'data\border_alerts.json') 
PATH = r'data\border_alerts.json'

def main():
    data = ReadData() 
    notifications: list = data.get_notification_data(PATH)
    # print(notification)
    for n in notifications:
        notification = Data(**n)
        print(notification)
    return notifications

if __name__ == "__main__":
    main()