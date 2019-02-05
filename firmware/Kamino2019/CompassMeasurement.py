try:
    from upm import pyupm_bmm150 as sensorObj
except ImportError:
    print('Error: Please install python-mraa python-upm module.\r\n'
          'See instruction here https://github.com/Seeed-Studio/pi_repo#mraa--upm-package-repository-for-raspberry-pi ')
import sys, signal, atexit, math

class CompassMeasurement:
    sensor = None

    def __init__(self):
        # Instantiate a BMP250E instance using default i2c bus and address
        self.sensor = sensorObj.BMM150(0, 0x13)

        # For SPI, bus 0, you would pass -1 as the address, and a valid pin for CS:
        # BMM150(0, -1, 10);

    def getHeadingDegrees(self):
        self.sensor.update()
        data = self.sensor.getMagnetometer()

        xyHeading = math.atan2(data[0], data[1])
        zxHeading = math.atan2(data[2], data[0])
        heading = xyHeading

        if heading < 0:
            heading += 2*math.pi
        if heading > 2*math.pi:
            heading -= 2*math.pi

        headingDegrees = heading * 180/(math.pi);
        xyHeadingDegrees = xyHeading * 180 / (math.pi)
        zxHeadingDegrees = zxHeading * 180 / (math.pi)

        return headingDegrees
