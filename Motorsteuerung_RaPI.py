import smbus

i2c_adress = 0x07 #Slave Adress vom Arduino
i2c_cmd = 0x01
bus = smbus.SMBus(1)

def ConvertIntToBytes(d, s, r): #Zahlen müssen in Bytes übertrgen werden
    converted = []
    converted.append(int.to_bytes(d))
    converted.append(int.to_bytes(s))
    converted.append(int.to_bytes(r))
    return converted


def move(d, s, r):      #d=directions(1,2,3,4); s=speed(255-0); r=rounds(how many rounds)
    bytesToSend = ConvertIntToBytes(d, s, r)
    bus.write_i2c_block_data(i2c_address, i2c_cmd, bytesToSend) #Bytes werden übertragen
