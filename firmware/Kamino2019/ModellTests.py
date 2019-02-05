import WorldModell as wm
import time

def start():
    world = wm.WorldModell()

    while True:
        world.updateSensors()
        print(world.isHeatVictim("R"))
        print("")
        time.sleep(1)
