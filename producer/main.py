import json


class ReadData:
    def get_notification_data(self, path):
        with open(path) as file:
            data = json.load(file)
            return data

