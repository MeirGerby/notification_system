# import os 

from priority_logic import ReadData, Data, Priority

# PATH = os.getenv('PATH', r'data\border_alerts.json') 
PATH = r'data\border_alerts.json'

def main():
    data = ReadData() 
    notifications: list = data.get_notification_data(PATH)
    # print(notification)
    for n in notifications:
        notification = Data(**n)
    proiriry = Priority(notifications)
    print(proiriry)
    return notifications

if __name__ == "__main__":
    main()