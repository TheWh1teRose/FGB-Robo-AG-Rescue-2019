#!/bin/bash
sshpass -p "robots1234" scp -rp ~/Documents/FGB-Robo-AG-Rescue-2019/firmware/rescue2019 pi@$1:RoboAG2019/firmware
