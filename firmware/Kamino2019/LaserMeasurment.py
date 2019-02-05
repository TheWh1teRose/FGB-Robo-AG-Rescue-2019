import VL53L0X

class LaserMeasurment:
    tof = None
    def __init__(self):
        self.tof = VL53L0X.VL53L0X()
        self.tof.start_ranging(VL53L0X.VL53L0X_BEST_ACCURACY_MODE)

    def getDistance(self):
        distance = self.tof.get_distance()
        return distance
