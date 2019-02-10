import RPi.GPIO as GPIO
import time
import logging


class ColorMeasurement:

    s2 = 23
    s3 = 24
    signal = 25
    NUM_CYCLES = 10


    def __init__(self):
      GPIO.setmode(GPIO.BCM)
      GPIO.setup(self.signal,GPIO.IN, pull_up_down=GPIO.PUD_UP)
      GPIO.setup(self.s2,GPIO.OUT)
      GPIO.setup(self.s3,GPIO.OUT)
      logging.debug("Color sensor setup success!")

    def getRed(self):
      temp = 1

      GPIO.output(self.s2,GPIO.LOW)
      GPIO.output(self.s3,GPIO.LOW)
      time.sleep(0.3)
      start = time.time()
      for impulse_count in range(self.NUM_CYCLES):
          GPIO.wait_for_edge(self.signal, GPIO.FALLING)
      duration = time.time() - start      #seconds to run for loop
      red  = self.NUM_CYCLES / duration   #in Hz
      return red
