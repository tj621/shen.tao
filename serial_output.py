'''

@author: Zxh
'''
# import serial

def println(value):
    print value
 
# serialport = serial.Serial("com3",9600,timeout=1)
# def init_serial(com):
#     serialport = serial.Serial("%s",9600,timeout=1 %(com))
 
# def send_data(data):
#     data=bytes.fromhex(data)
#     serialport.write(data)
#     print(data)
#     receive=serialport.readall()
#     print(receive)
#  
# init_serial('com1')
# data="FE 05 00 05 00 00 C9 C4"
# while True:
#     send_data(data)