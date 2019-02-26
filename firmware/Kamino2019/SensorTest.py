import Sensors
from time import sleep

sensorPins = {"temper": [(0,1)], "ultrasonic": [6]}

sensors = Sensors.Sensors(sensorPins)

while True:
    print("Temperatur")
    #if surrounding temperatur = 11.6146642126 and object temperatur = 36.3025070917 is sensor not connected
    for pins in sensorPins["temper"]:
        pin, _ = pins
        print("Pin: " + str(pin))
        print("   "+str(sensors.getSurrTemper(0)))
        print("   "+str(sensors.getObjTemper(0)))
    print("Ultraschall")
    for pin in sensorPins["ultrasonic"]:
        print("Pin: " + str(sensors.getUltrasonicDist(pin)))
    print("Compass")
    print(sensors.getCompassHeading())
    print("LaserDist")
    print(sensors.getLaserDist())
    print("\n")
    sleep(1)
