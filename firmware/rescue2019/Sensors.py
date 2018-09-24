import grovepi as gp
from time import sleep
import numpy as np
import TemperaturMeasurement


class Sensors:
    """Class that contains all nessesary Functions to get the sonsordata from the Robot"""

    temperMeas = []

    def __init__(self, pins):
        """Set up the Sonsors and create sensor objects

        Parameters:
            pins (dict): A dictionary that contains the pin information. Format like: ['temper': [(1,2), (3,4)], 'ultrasonic': [5,6,7], 'other': [1,2,3,4]]
        """
        temperPins = pins['temper']
        for pin1, pin2 in temperPins:
            self.temperMeas.append(TemperaturMeasurement.TemperaturMeasurement([pin1, pin2]))

    def getSurrTemper(self, pin):
        """Get the surrounding temperatur from an infared temperatur sensorself.

        Parameters:
            pin (int):  The index in the dictionary. Starting with 0.

        Returns:
            float: The surrounding temperatur. Note: no reale scale (not in Celsius) normal Temperatur ~ 68
        """
        temper = self.temperMeas[pin].measureSurTemp()
        return temper

    def getObjTemper(self, pin):
        """Get the object temperatur from an infared temperatur sensorself.

        Parameters:
            pin (dict): A dictionary with tow int that represent the pins of the sensor.

        Returns:
            float: The object temperatur. Note: no reale scale (not in Celsius) normal Temperatur ~ 68
        """
        temper = self.temperMeas[pin].measureObjectTemp()
        return temper

    def getUltrasonicDist(self, pin):
        """Get the distance from an ultrasonic sensor

        Parameters:
            pin (int): The pin where the sensor is connected

        Returns:
            int: The distance the sensor sees
        """
        dist = gp.ultrasonicRead(pin)
        return dist
