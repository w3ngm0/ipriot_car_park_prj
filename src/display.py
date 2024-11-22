
class Display:
    ...
    """ Constructors below, id and car_park has no default value"""
    def __init__(self, id, car_park, message="", is_on=False):
        self.id = id
        self.car_park = car_park
        self.message = message
        self.is_on = is_on

    """ Method will be called when printing a Display object. Method should return string 
    with display Id and message. "Display 1: Welcome to the car park."""
    def __str__(self):
        ...
