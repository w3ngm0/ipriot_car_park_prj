"""
Car Park Class below with imports from Sensor and Display class
"""
from sensor import Sensor
from display import Display

class CarPark:
    # Constructors
    def __init__(self, location="Unknown", capacity="Unknown", plates=None, sensors=None, displays=None):
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

