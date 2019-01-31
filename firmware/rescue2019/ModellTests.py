import WorldModell as wm
import time

world = wm.WorldModell()
print("lol")

while True:
    world.updateSensors()
    print(world.isHeatVictim("R"))
    print("")
    time.sleep(1)
