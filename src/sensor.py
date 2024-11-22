class Sensor:
    """
    Constructor method for Sensor class.
    """
    def __init__(self, id, is_active, car_park):
        self.id = id
        self.is_active = is_active
        self.car_park = car_park

    def __str__(self):
        ...  # Return string containing sensor's id and status

    """need subclass Entry and Exit for sensor"""


class EntrySensor(Sensor):
    ...


class ExitSensor(Sensor):
    ...

