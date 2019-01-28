import Sensors
import numpy as np
import sys, os

## TODO:
## method: get raw distance -> norm values on cm, return -1 on to large numbers
## method: is obstical
## method: is heat object

class WorldModell:
    saveLenght = 10

    sensors = None
    sensorValues = {
    "distF": np.zeros(saveLenght),
    "distR": np.zeros(saveLenght),
    "distL": np.zeros(saveLenght),
    "temSurR": np.zeros(saveLenght),
    "temObjR": np.zeros(saveLenght),
    "temSurL": np.zeros(saveLenght),
    "temObjL": np.zeros(saveLenght),
    "comp": np.zeros(saveLenght)
    }
    def __init__(self):
        sensorPins = {"temper": [(0,1)], "ultrasonic": [6]}
        self.sensors = Sensors.Sensors(sensorPins)

    def updateSensors(self):
        #update laser values in front
        distF = np.roll(self.sensorValues["distF"], 1)
        distFVal = self.sensors.getLaserDist()/10
        distF[0] = distFVal
        self.sensorValues["distF"] = distF

        #update ultrasonic values right
        distR = np.roll(self.sensorValues["distR"], 1)
        distRVal = self.sensors.getUltrasonicDist(6)
        distR[0] = distRVal
        self.sensorValues["distR"] = distR

        #update ultrasonic values right
        #distL = np.roll(self.sensorValues["distL"], 1)
        #distLVal = self.sensors.getUltrasonicDist(7)
        #distL[0] = distLVal
        #self.sensorValues["distL"] = distL

        #update temp values right
        #surrounding temp
        tempSurR = np.roll(self.sensorValues["tempSurR"], 1)
        tempSurRVal = self.sensors.getSurrTemper(0)
        tempSurR[0] = tempSurRVal
        self.sensorValues["tempSurR"] = tempSurR
        #object temp
        tempObjR = np.roll(self.sensorValues["tempObjR"], 1)
        tempObjRVal = self.sensors.getObjTemper(1)
        tempObjR[0] = tempObjRVal
        self.sensorValues["tempObjR"] = tempObjR

    def getRawDist(self, direction):
        if direction=="F":
            dist = self.sensorValues["distF"][0]
            return dist
        elif direction=="R":
            dist = self.sensorValues["distR"][0]
            return dist
        #elif direction=="L":
            #dist = self.sensorValues["distL"][0]
            #return dist
    def isObstical(self, direction):
        thresholdLaser = 15
        thresholdUS = 10
        if direction=="F":
            obst = self.sensorValues["distF"][0] < thresholdLaser
            return obst
        elif direction=="R":
            obst = self.sensorValues["distR"][0] < thresholdUS
            return obst
        #elif direction=="L":
            #obst = True if self.sensorValues["distL"][0] < thresholdUS else False
            #return obst

    def isHeatViction(self, direction):
        heatThreshold = 10
        if direction=="R":
            heatDiff = self.sensorValues["tempSurR"] - self.sensorValues["tempObjR"]
            return heatDiff > heatThreshold
        elif direction=="L":
            heatDiff = self.sensorValues["tempSurL"] - self.sensorValues["tempObjL"]
            return heatDiff > heatThreshold
