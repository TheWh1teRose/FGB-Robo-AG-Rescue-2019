import Sensors
import numpy as np

## TODO:
## method: get raw distance -> norm values on cm, return -1 on to large numbers
## method: is obstical
## method: is heat object

class WorldModell:
    saveLenght = 10

    sensors = None
    sensorValues = {
    "usF": np.zeros(saveLenght),
    "usR": np.zeros(saveLenght),
    "usL": np.zeros(saveLenght),
    "temR": np.zeros(saveLenght),
    "temL": np.zeros(saveLenght),
    "comp": np.zeros(saveLenght)
    }
    def __init__(self):
        sensorPins = {"temper": [(0,1)], "ultrasonic": [6]}
        self.sensors = Sensors.Sensors(sensorPins)

    def updateSensors(self):

    def getRawDist(self, direction):
        if direction=="F":
            dist = self.sensors.getLaserDist()
            return dist
        elif direction=="R":
            dist = self.sensors.getUltrasonicDist(6)
            return dist
        #elif direction=="L":
            #dist = self.sensors.getUltrasonicDist(7)
            #return dist
    def isObstical(self, direction):
        if direction=="F":
            dist = self.sensors.getLaserDist()
            return dist
        elif direction=="R":
            dist = self.sensors.getUltrasonicDist(6)
            return dist
        #elif direction=="L":
            #dist = self.sensors.getUltrasonicDist(7)
            #return dist
