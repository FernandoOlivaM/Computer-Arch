from time import sleep          #import

import RPi.GPIO as GPIO
import requests
import json
  
# defining the api-endpoint 
API_ENDPOINT = "https://i7dc18qycl.execute-api.us-east-2.amazonaws.com/Connection/connection"

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(26, GPIO.IN) #set pin de entrada para contador

GPIO.setup(21, GPIO.OUT) #set pin de salida
GPIO.setup(20, GPIO.OUT) #set pin de salida
GPIO.setup(16, GPIO.OUT) #set pin de salida
GPIO.setup(12, GPIO.OUT) #set pin de salida
GPIO.setup(1, GPIO.OUT) #set pin de salida
GPIO.setup(7, GPIO.OUT) #set pin de salida
GPIO.setup(8, GPIO.OUT) #set pin de salida
GPIO.setup(25, GPIO.OUT) #set pin de salida, relay

contador = 1 #variable para contador de entradas

def reset():
    GPIO.output(21, False)
    GPIO.output(20, False)
    GPIO.output(16, False)
    GPIO.output(12, False)
    GPIO.output(1, False)
    GPIO.output(7, False)
    GPIO.output(8, False)
    GPIO.output(25, False)
reset()
while True:
    
    
    if(contador >10):
        contador = 1
    x = {
    "contador": contador,
    "dispositivo": "Raspberry"
    }
    
    if GPIO.input(26):
        reset()
        contador +=1
        r = requests.post(url = API_ENDPOINT, data = json.dumps(x))
        response = json.loads(r.text)
        display =response['display']
        if ((display[0])=='1'):
            GPIO.output(21, True)
            
        if (str(display[1])=='1'):
            GPIO.output(20, True)
            
        if (str(display[2])=='1'):
            GPIO.output(16, True)
            
        if (str(display[3])=='1'):
            GPIO.output(12, True)
            
        if (str(display[4])=='1'):
            GPIO.output(1, True)
            
        if (str(display[5])=='1'):
            GPIO.output(7, True)
            
        if (str(display[6])=='1'):
            GPIO.output(8, True)
        #relay
        if (str(display[7])=='1'):
            GPIO.output(25, True)
            
        print("The pastebin URL is:%s"%str(display))