import WorldModell as wm
import time

world = wm.WorldModell()
print("lol")

while True:
    world.updateSensors()
    print(world.isObstical("F"))
    print(world.isObstical("R"))
    print(world.getRawDist("F"))
    print(world.getRawDist("R"))
    print("")
    time.sleep(1)
