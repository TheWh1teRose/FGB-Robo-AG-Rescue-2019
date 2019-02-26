import Sensors
import numpy as np
import sys, os
import logging

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
    "tempSurR": np.zeros(saveLenght),
    "tempObjR": np.zeros(saveLenght),
    "tempSurL": np.zeros(saveLenght),
    "tempObjL": np.zeros(saveLenght),
    "comp": np.zeros(saveLenght),
    "color": np.zeros(saveLenght)
    }
    def __init__(self):
        sensorPins = {"temper": [(0,1), (2,3)], "ultrasonic": [6, 5]}
        self.sensors = Sensors.Sensors(sensorPins)

    def updateSensors(self):
        #update laser values in front
        distF = np.roll(self.sensorValues["distF"], 1)
        distFVal = self.sensors.getLaserDist("F")/10
        distF[0] = distFVal
        self.sensorValues["distF"] = distF

        #update ultrasonic values right
        distR = np.roll(self.sensorValues["distR"], 1)
        distRVal = self.sensors.getLaserDist("R")/10
        distR[0] = distRVal
        self.sensorValues["distR"] = distR

        #update ultrasonic values right
        #distL = np.roll(self.sensorValues["distL"], 1)
        #distLVal = self.sensors.getLaserDist("L")/10
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
        tempObjRVal = self.sensors.getObjTemper(0)
        tempObjR[0] = tempObjRVal
        self.sensorValues["tempObjR"] = tempObjR

        #update temp values left
        #surrounding temp
        tempSurL = np.roll(self.sensorValues["tempSurR"], 1)
        tempSurLVal = self.sensors.getSurrTemper(1)
        tempSurL[0] = tempSurLVal
        self.sensorValues["tempSurL"] = tempSurL
        #object temp
        tempObjL = np.roll(self.sensorValues["tempObjL"], 1)
        tempObjLVal = self.sensors.getObjTemper(1)
        tempObjL[0] = tempObjLVal
        self.sensorValues["tempObjL"] = tempObjL

        #update compass values
        comp = np.roll(self.sensorValues["comp"], 1)
        compVal = self.sensors.getCompassHeading()
        comp[0] = compVal
        self.sensorValues["comp"] = comp

        #update color sensor
        color = np.roll(self.sensorValues["color"], 1)
        colorVal = self.sensors.getColorIntensity()
        color[0] = colorVal
        self.sensorValues["color"] = color

        #logging sensor values
        logging.info("Sensor data\n Dists(L,F,R): %s; %s; %s\n Temp(SL,OL, SR, OR): %s; %s;; %s; %s\nComp: %s\nColor: %s", 0, distFVal, distRVal, tempSurRVal, tempObjRVal, tempSurLVal, tempObjLVal, compVal, colorVal)

    def getRawDist(self, direction):
        if direction=="F":
            dist = self.sensorValues["distF"][0]
            return dist
        elif direction=="R":
            dist = self.sensorValues["distR"][0]
            return dist
        elif direction=="L":
            dist = self.sensorValues["distL"][0]
            return dist
    def isObstical(self, direction):
        thresholdLaser = 15
        thresholdUS = 10
        if direction=="F":
            obst = self.sensorValues["distF"][0] < thresholdLaser
            return obst
        elif direction=="R":
            obst = self.sensorValues["distR"][0] < thresholdUS
            return obst
        elif direction=="L":
            obst = self.sensorValues["distL"][0] < thresholdUS
            return obst

    def isHeatVictim(self, direction):
        heatThreshold = 2
        if direction=="R":
            heatDiff = abs(self.sensorValues["tempSurR"][0] - self.sensorValues["tempObjR"][0])
            return heatDiff > heatThreshold
        elif direction=="L":
            heatDiff = abs(self.sensorValues["tempSurL"][0] - self.sensorValues["tempObjL"][0])
            return heatDiff > heatThreshold

    def getRawHeading(self):
        return self.sensorValues["comp"][0]

    def isBlack(self):
        threshold = 10000
        return self.sensorValues["color"][0] < threshold
