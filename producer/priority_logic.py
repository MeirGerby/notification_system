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

    def _check_if_weapons(self, notification: Data) -> bool:
        """checks if there's weapon in there """
        return notification.weapons_count > 0
    
    def _check_distance_from_fence_m(self, notification: Data) -> bool:
        """check if the distance is 50 meter less than"""
        return notification.distance_from_fence_m <= 50
    
    def _check_people_count(self, notification: Data) -> bool:
        """check if there is 8 poeple or less"""
        return notification.people_count >= 8
     
    def _check_vehicle_type(self, notification: Data) -> bool:
        """check if the vehicle_type is truck"""
        return notification.vehicle_type == 'truck'
    
    def _check_distance_and_people(self, notification: Data) -> bool:
        """check if the distance is 150 or less and people count is 4 or more poeple"""
        return notification.distance_from_fence_m <= 150 and notification.people_count >= 4 
        
    def _check_vehicle_and_people(self, notification: Data) -> bool:
        """check if the vehicle_type is jeep and people count is 3 or more poeple"""
        return notification.vehicle_type == 'jeep' and notification.people_count >= 3 
    
    
    def _add_priority_field(self,notification: Data, priority):
        """add a priority field to a notification based on the priority it gets"""
        if priority == 'URGENT':
            notification.priority = 'URGENT'
        elif priority == 'NORMAL':
            notification.priority = 'NORMAL' 

    def check_notification(self):
        """the main function for checking the notification priority type"""
        urgent = 'URGENT'
        normal = 'NORMAL'
        for n in self.notifications:
            if self._check_if_weapons(n):
                self._add_priority_field(n, urgent)

            elif self._check_distance_from_fence_m(n):
                self._add_priority_field(n, urgent)

            elif self._check_people_count(n):
                self._add_priority_field(n, urgent)
                
            elif self._check_vehicle_type(n):
                self._add_priority_field(n, urgent)

            elif self._check_distance_and_people(n):
                self._add_priority_field(n, urgent)

            elif self._check_vehicle_and_people(n):
                self._add_priority_field(n, urgent)
            else: 
                self._add_priority_field(n, normal) 
    
    def __iter__(self):
        return iter(self.notifications)
                


