import VL53L0X

class LaserMeasurment:
    tofF = None
    tofL = None
    tofR = None
    def __init__(self):
        self.tofF = VL53L0X.VL53L0X(TCA9548A_Num=1, TCA9548A_Addr=0x70)
        self.tofR = VL53L0X.VL53L0X(TCA9548A_Num=2, TCA9548A_Addr=0x70)
        #self.tofL = VL53L0X.VL53L0X(TCA9548A_Num=3, TCA9548A_Addr=0x70)
        self.tofF.start_ranging(VL53L0X.VL53L0X_BEST_ACCURACY_MODE)
        self.tofR.start_ranging(VL53L0X.VL53L0X_BEST_ACCURACY_MODE)
        #self.tofL.start_ranging(VL53L0X.VL53L0X_BEST_ACCURACY_MODE)

    def getDistance(self, direction):
        if direction == "F":
            distance = self.tofF.get_distance()
            return distance
        elif direction == "R":
            distance = self.tofR.get_distance()
            return distance
        #elif direction = "L":
        #    distance = self.tofL.get_distance()
        #    return distance
