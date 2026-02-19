import json
from typing import List

class ReadData:
    def get_notification_data(self, path) -> list:
        """read a json file and return a list object"""
        with open(path) as file:
            data = json.load(file)
            return data
class Data:
    def __init__(self, border, zone, timestamp, people_count, weapons_count, vehicle_type, distance_from_fence_m, visibility_quality, priority=None):
        self.border  = border
        self.zone  = zone
        self.timestamp  = timestamp
        self.people_count  = people_count
        self.weapons_count  = weapons_count
        self.vehicle_type  = vehicle_type
        self.distance_from_fence_m  = distance_from_fence_m
        self.visibility_quality  = visibility_quality 
        self.priority = priority

    def __repr__(self): 
        return f'''
            border: {self.border}, 
            zone: {self.zone}, 
            timestamp: {self.timestamp}, 
            people_count: {self.people_count}, 
            weapons_count: {self.weapons_count}, 
            vehicle_type: {self.vehicle_type}, 
            distance_from_fence_m: {self.distance_from_fence_m}, 
            visibility_quality: {self.visibility_quality}'''

class Priority:
    def __init__(self, notifications: List[Data]):
        self.notifications = notifications 

    def check_if_weapons(self, notification: Data) -> bool:
        """checks if there's weapon in there """
        return notification.weapons_count > 0
    
    def check_distance_from_fence_m(self, notification: Data) -> bool:
        """check if the distance is 50 meter less than"""
        return notification.distance_from_fence_m <= 50
    
    def check_people_count(self, notification: Data) -> bool:
        """check if there is 8 poeple or less"""
        return notification.people_count >= 8
     
    def check_vehicle_type(self, notification: Data) -> bool:
        """check if the vehicle_type is truck"""
        return notification.vehicle_type == 'truck'
    
    def check_distance_and_people(self, notification: Data) -> bool:
        """check if the distance is 150 or less and people count is 4 or more poeple"""
        return notification.distance_from_fence_m <= 150 and notification.people_count >= 4 
        
    def check_vehicle_and_people(self, notification: Data) -> bool:
        """check if the vehicle_type is jeep and people count is 3 or more poeple"""
        return notification.vehicle_type == 'jeep' and notification.people_count >= 3 
    
    
    def add_priority_field(self, priority, notification: Data):
        if priority == 'URGENT':
            notification.priority = 'URGENT'
        elif priority == 'NORMAL':
            notification.priority = 'NORMAL' 

        


    
