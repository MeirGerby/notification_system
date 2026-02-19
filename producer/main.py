# import os 

from priority_logic import ReadData

# PATH = os.getenv('PATH', r'data\border_alerts.json') 
PATH = r'data\border_alerts.json'

def main():
    data = ReadData() 
    notification = data.get_notification_data(PATH)
    print(notification)
    return notification

if __name__ == "__main__":
    main()