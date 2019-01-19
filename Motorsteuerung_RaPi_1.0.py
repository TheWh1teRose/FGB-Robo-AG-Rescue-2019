import smbus

bus = smbus.SMBus(1)
i2c_adress = 0x07 #Slave Adress vom Arduino
i2c_cmd = 0x01

list = []


def CreateListM(d, s): #Zahlen werden an Liste übergeben
    #list.append(0)  #Order (0 == Motoren gestartet --> geradeaus fahren)
    list.append(d)
    list.append(s)
    return list

def CreateListR(d, s, r): #Zahlen werden an Liste übergeben
    #list.append(2)  #Order (2 == Move Rounds)
    list.append(d)
    list.append(s)
    list.append(r)
    return list

def move(d,s):      #d=directions(1,2); s=speed(255-0)
    listToSend = CreateListM(d, s)
    bus.write_i2c_block_data(i2c_address, i2c_cmd, listToSend) #Liste wird übertragen
    print(listToSend)

def stop():
    listToSend = []
    #listToSend = [1]  #Order (1 == Motoren stopp)
    bus.write_i2c_block_data(i2c_address, i2c_cmd, listToSend) #Liste wird übertragen
    print(listToSend)

def moveR(d, s, r):      #d=directions(1,2); s=speed(255-0); r=rounds(how many rounds)
    listToSend = CreateListR(d, s, r)
    bus.write_i2c_block_data(i2c_address, i2c_cmd, listToSend) #Liste wird übertragen
    print(listToSend)

def turn(d):
    listToSend = [d]
