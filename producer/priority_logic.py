import json

class ReadData:
    def get_notification_data(self, path):
        with open(path) as file:
            data = json.load(file)
            return data
class Data:
    def __init__(self, border, zone, timestamp, people_count, weapons_count, vehicle_type, distance_from_fence_m, visibility_quality):
        self.border  = border
        self.zone  = zone
        self.timestamp  = timestamp
        self.people_count  = people_count
        self.weapons_count  = weapons_count
        self.vehicle_type  = vehicle_type
        self.distance_from_fence_m  = distance_from_fence_m
        self.visibility_quality  = visibility_quality


# class Priority: