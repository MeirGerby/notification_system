import json

with open(r'data\border_alerts.json') as file:
    data = json.load(file)
    print(data)