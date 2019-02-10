import logging
import sys
import time

from Adafruit_BNO055 import BNO055

class CompassMeasurement:
    bno = None

    def __init__(self):

        self.bno = BNO055.BNO055(serial_port='/dev/serial0', rst=18)

        # Initialize the self.bno055 and stop if something went wrong.
        if not self.bno.begin():
            raise RuntimeError('Failed to initialize bno055! Is the sensor connected?')

        # logging.debug system status and self test result.
        status, self_test, error = self.bno.get_system_status()
        logging.debug('System status: {0}'.format(status))
        logging.debug('Self test result (0x0F is normal): 0x{0:02X}'.format(self_test))
        # logging.debug out an error if system status is in error mode.
        if status == 0x01:
            logging.debug('System error: {0}'.format(error))
            logging.debug('See datasheet section 4.3.59 for the meaning.')

        # logging.debug self.bno055 software revision and other diagnostic data.
        sw, bl, accel, mag, gyro = self.bno.get_revision()
        logging.debug('Software version:   {0}'.format(sw))
        logging.debug('Bootloader version: {0}'.format(bl))
        logging.debug('Accelerometer ID:   0x{0:02X}'.format(accel))
        logging.debug('Magnetometer ID:    0x{0:02X}'.format(mag))
        logging.debug('Gyroscope ID:       0x{0:02X}\n'.format(gyro))

    def getHeadingDegrees(self):
        heading, roll, pitch = self.bno.read_euler()
        return heading
