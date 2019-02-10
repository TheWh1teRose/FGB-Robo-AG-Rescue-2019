import grovepi as gp
from time import sleep
import numpy as np
import CompassMeasurement
import TemperaturMeasurement
import LaserMeasurment
import ColorMeasurement


class Sensors:
    """Class that contains all nessesary Functions to get the sonsordata from the Robot"""

    temperMeas = []
    compassMeas = None
    laserMeas = None
    colorMeas = None

    def __init__(self, pins):
        """Set up the Sonsors and create sensor objects

        Parameters:
            pins (dict): A dictionary that contains the pin information. Format like: ['temper': [(1,2), (3,4)], 'ultrasonic': [5,6,7], 'other': [1,2,3,4]]
        """
        #set up temperatur sensors
        temperPins = pins['temper']
        for pin1, pin2 in temperPins:
            self.temperMeas.append(TemperaturMeasurement.TemperaturMeasurement([pin1, pin2]))

        #set up Compass
        self.compassMeas = CompassMeasurement.CompassMeasurement()

        #set up Laser Measurment
        self.laserMeas = LaserMeasurment.LaserMeasurment()

        #set up color Measurement
        self.colorMeas = ColorMeasurement.ColorMeasurement()

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

    def getCompassHeading(self):
        """Get the degrees the compass is heading

        Parameters:
            None

        Returns:
            float: The degrees the compass is heading
        """
        headingDegrees = self.compassMeas.getHeadingDegrees()
        return headingDegrees

    def getLaserDist(self, direction):
        """Get the distance from the laser

        Parameters:
            None

        Returns:
            float: Distance in mm
        """
        dist = self.laserMeas.getDistance(direction)
        return dist

    def getColorIntensity(self):
        """Get the intensity of the Red color

        Parameters:
            None

        Returns:
            int: Intensity
        """
        return self.colorMeas.getRed()
