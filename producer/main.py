import json
import os 

PATH = os.getenv(PATH, r'data\border_alerts.json') # type: ignore
class ReadData:
    def get_notification_data(self, path):
        with open(path) as file:
            data = json.load(file)
            return data

