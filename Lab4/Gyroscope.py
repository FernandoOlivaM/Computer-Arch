import smbus#
from time import sleep          #import
import requests
import json
  
# defining the api-endpoint 
API_ENDPOINT = "https://i7dc18qycl.execute-api.us-east-2.amazonaws.com/Connection/connection"

#some MPU6050 Registers and their Address
PWR_MGMT_1   = 0x6B
SMPLRT_DIV   = 0x19
CONFIG       = 0x1A
GYRO_CONFIG  = 0x1B
INT_ENABLE   = 0x38
ACCEL_XOUT_H = 0x3B
ACCEL_YOUT_H = 0x3D
ACCEL_ZOUT_H = 0x3F
GYRO_XOUT_H  = 0x43
GYRO_YOUT_H  = 0x45
GYRO_ZOUT_H  = 0x47


def MPU_Init():
    #write to sample rate register
    bus.write_byte_data(Device_Address, SMPLRT_DIV, 7)
    
    #Write to power management register
    bus.write_byte_data(Device_Address, PWR_MGMT_1, 1)
    
    #Write to Configuration register
    bus.write_byte_data(Device_Address, CONFIG, 0)
    
    #Write to Gyro configuration register
    bus.write_byte_data(Device_Address, GYRO_CONFIG, 24)
    
    #Write to interrupt enable register
    bus.write_byte_data(Device_Address, INT_ENABLE, 1)
def read_raw_data(addr):
    #Accelero and Gyro value are 16-bi
        high = bus.read_byte_data(Device_Address, addr)
        low = bus.read_byte_data(Device_Address, addr+1)
    
        #concatenate higher and lower value
        value = ((high << 8) | low)
        
        #to get signed value from mpu6050
        if(value > 32768):
                value = value - 65536
        return value


bus = smbus.SMBus(1)# or bus = smbus.SMBus(0) for older version boards
Device_Address = 0x68   # MPU6050 device address

MPU_Init()
def writeData(message,status):
    print(message + status)
    x = {
        "message": message,
        "status": status
        }
    # sending post request and saving response as response object
    r = requests.post(url = API_ENDPOINT, data = json.dumps(x))
while True:

    
    #Read Gyroscope raw value
    gyro_x = read_raw_data(GYRO_XOUT_H)
    gyro_y = read_raw_data(GYRO_YOUT_H)
    gyro_z = read_raw_data(GYRO_ZOUT_H)
        
    Gx = gyro_x/13.0
    Gy = gyro_y/13.0
    Gz = gyro_z/13.0

    
    if(Gx>0 and Gx <10):
        writeData("ESTADO CORRECTO A LA DERECHA ","Gx:"+'{0:.2f}'.format(Gx)+", Gy:"+'{0:.2f}'.format(Gy)+", Gz:"+'{0:.2f}'.format(Gz))
        
    if(Gx>-10 and Gx <0):
        writeData("ESTADO CORRECTO A LA IZQUIERDA ","Gx:"+'{0:.2f}'.format(Gx)+", Gy:"+'{0:.2f}'.format(Gy)+", Gz:"+'{0:.2f}'.format(Gz))
        
    if(Gx>10):
        writeData("ERROR EL AVION ESTA MUY A LA DERECHA","Gx:"+'{0:.2f}'.format(Gx)+", Gy:"+'{0:.2f}'.format(Gy)+", Gz:"+'{0:.2f}'.format(Gz))
        
    if(Gx<-10):
        writeData("ERROR EL AVION ESTA MUY A LA IZQUIERDA ","Gx:"+'{0:.2f}'.format(Gx)+", Gy:"+'{0:.2f}'.format(Gy)+", Gz:"+'{0:.2f}'.format(Gz))
        
    if(Gy>0 and Gy <10):
        writeData("ESTADO CORRECTO DE NARIZ DEL AVION ","Gx:"+'{0:.2f}'.format(Gx)+", Gy:"+'{0:.2f}'.format(Gy)+", Gz:"+'{0:.2f}'.format(Gz))
        
    if(Gy>-10 and Gy <0):
        writeData("ESTADO CORRECTO DE NARIZ DEL AVION ","Gx:"+'{0:.2f}'.format(Gx)+", Gy:"+'{0:.2f}'.format(Gy)+", Gz:"+'{0:.2f}'.format(Gz))
    if(Gy>10):
        writeData("ERROR EL AVION ESTA CON NARIZ ARRIBA ","Gx:"+'{0:.2f}'.format(Gx)+", Gy:"+'{0:.2f}'.format(Gy)+", Gz:"+'{0:.2f}'.format(Gz))
        
    if(Gy<-10):
        writeData("ERROR EL AVION ESTA CON NARIZ ABAJO ","Gx:"+'{0:.2f}'.format(Gx)+", Gy:"+'{0:.2f}'.format(Gy)+", Gz:"+'{0:.2f}'.format(Gz))
    sleep(1)
    


