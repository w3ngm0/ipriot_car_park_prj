"""
Car Park Class below
"""


class CarPark:
    # Constructors
    location = "Unknown"
    capacity = "Unknown"

    def __init__(self, location, capacity, plates=None, sensors=None, displays=None):
        self.location = location
        self.capacity = capacity
        self.plates = plates or []
        self.sensors = sensors or []
        self.displays = displays or []

    """
    Method caled when printing a car park 'object'. Method should also return string 
    containing car park's location and capacity. For eg. "Car park at ___ street, with __ bays."
    """
    def __str__(self):
        ... # Return a string containing the car park's location and capacity
