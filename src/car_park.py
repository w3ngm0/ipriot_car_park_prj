"""
Car Park Class below with imports from Sensor and Display class
"""
from sensor import Sensor
from display import Display
from datetime import datetime

class CarPark:
    # Constructors
    def __init__(self, location="Unknown", capacity=0, plates=None, sensors=None,
                 displays=None):
        self.location = location
        self.capacity = capacity
        self.plates = plates or []
        self.sensors = sensors or []
        self.displays = displays or []

    """
    Method called when printing a car park 'object'. Method should also return string 
    containing car park's location and capacity. For eg. "Car park at ___ street, with __ bays."
    """
    def __str__(self):
        ...  # Return a string containing the car park's location and capacity

    # def register(self, component):
    #     if not isinstance(component, (Sensor, Display)):
    #         raise TypeError("Object must be a Sensor or Display")

    def register(self, component):
        """ This method will allow car park to register sensors and displays

        """
        if isinstance(component, Sensor):
            self.sensors.append(component)
        elif isinstance(component, Display):
            self.displays.append(component)
        else:
            raise TypeError("Object must be a Sensor or Display")

    # adding property decorator for available bays
    @property
    def available_bays(self):
        """ Calculates the number of available bays in the car park.
        """
        if len(self.plates) < self.capacity:
            return self.capacity - len(self.plates)
        else:
            return 0

    def update_displays(self):

        """Updates  information for available bays, temperature and other information like
        time."""

        data = {"available_bays": self.available_bays,
                "temperature": 25,
                "time": datetime.time}
        for display in self.displays:
            display.update(data)

    def add_car(self, plate):
        self.plates.append(plate)
        self.update_displays()

    def remove_car(self, plate):
        self.plates.append(plate)
        self.update_displays()



