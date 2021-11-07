from time import sleep          #import
from datetime import datetime
import RPi.GPIO as GPIO
import requests
import json
  
# defining the api-endpoint 
API_ENDPOINT = "https://i7dc18qycl.execute-api.us-east-2.amazonaws.com/Connection/connection"

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
#emisor receptor
GPIO.setup(26, GPIO.IN) #set pin de entrada para contador
#dip switch
GPIO.setup(19, GPIO.IN) #set pin swtich 1
GPIO.setup(13, GPIO.IN) #set pin swtich 2
GPIO.setup(6, GPIO.IN) #set pin swtich 3
GPIO.setup(5, GPIO.IN) #set pin swtich 4

#display 1
GPIO.setup(21, GPIO.OUT) #set pin de salida
GPIO.setup(20, GPIO.OUT) #set pin de salida
GPIO.setup(16, GPIO.OUT) #set pin de salida
GPIO.setup(12, GPIO.OUT) #set pin de salida
GPIO.setup(1, GPIO.OUT) #set pin de salida
GPIO.setup(7, GPIO.OUT) #set pin de salida
GPIO.setup(8, GPIO.OUT) #set pin de salida

#display 2
GPIO.setup(25, GPIO.OUT) #set pin de salida
GPIO.setup(24, GPIO.OUT) #set pin de salida
GPIO.setup(23, GPIO.OUT) #set pin de salida
GPIO.setup(18, GPIO.OUT) #set pin de salida
GPIO.setup(15, GPIO.OUT) #set pin de salida
GPIO.setup(14, GPIO.OUT) #set pin de salida
GPIO.setup(2, GPIO.OUT) #set pin de salida

#display 3
GPIO.setup(3, GPIO.OUT) #set pin de salida
GPIO.setup(4, GPIO.OUT) #set pin de salida
GPIO.setup(17, GPIO.OUT) #set pin de salida
GPIO.setup(27, GPIO.OUT) #set pin de salida
GPIO.setup(22, GPIO.OUT) #set pin de salida
GPIO.setup(10, GPIO.OUT) #set pin de salida
GPIO.setup(9, GPIO.OUT) #set pin de salida

#puntos
GPIO.setup(0, GPIO.OUT) #set pin de salida
GPIO.setup(11, GPIO.OUT) #set pin de salida

contador = 0 #variable para contador de entradas

def reset():
    GPIO.output(21, False) #set pin de salida
    GPIO.output(20, False) #set pin de salida
    GPIO.output(16, False) #set pin de salida
    GPIO.output(12, False) #set pin de salida
    GPIO.output(1, False) #set pin de salida
    GPIO.output(7, False) #set pin de salida
    GPIO.output(8, False) #set pin de salida

    #display 2
    GPIO.output(25, False) #set pin de salida
    GPIO.output(24, False) #set pin de salida
    GPIO.output(23, False) #set pin de salida
    GPIO.output(18, False) #set pin de salida
    GPIO.output(15, False) #set pin de salida
    GPIO.output(14, False) #set pin de salida
    GPIO.output(2, False) #set pin de salida

    #display 3
    GPIO.output(3, False) #set pin de salida
    GPIO.output(4, False) #set pin de salida
    GPIO.output(17, False) #set pin de salida
    GPIO.output(27, False) #set pin de salida
    GPIO.output(22, False) #set pin de salida
    GPIO.output(10, False) #set pin de salida
    GPIO.output(9, False) #set pin de salida
    #puntos
    GPIO.output(0, False) #set pin de salida
    GPIO.output(11, False) #set pin de salida    
         
reset()
def drawD1(number):
    if (number==0):
        GPIO.output(21, True) #a
        GPIO.output(20, True) #b
        GPIO.output(16, True) #c
        GPIO.output(12, True) #d
        GPIO.output(1, True) #e
        GPIO.output(7, True) #f
        GPIO.output(8, False) #g
    elif (number==1):
        GPIO.output(21, False) #a
        GPIO.output(20, True) #b
        GPIO.output(16, True) #c
        GPIO.output(12, False) #d
        GPIO.output(1, False) #e
        GPIO.output(7, False) #f
        GPIO.output(8, False) #g
    elif (number==2):
        GPIO.output(21, True) #a
        GPIO.output(20, True) #b
        GPIO.output(16, False) #c
        GPIO.output(12, True) #d
        GPIO.output(1, True) #e
        GPIO.output(7, False) #f
        GPIO.output(8, True) #g
    elif (number==3):
        GPIO.output(21, True) #a
        GPIO.output(20, True) #b
        GPIO.output(16, True) #c
        GPIO.output(12, True) #d
        GPIO.output(1, False) #e
        GPIO.output(7, False) #f
        GPIO.output(8, True) #g 
    elif (number==4):
        GPIO.output(21, False) #a
        GPIO.output(20, True) #b
        GPIO.output(16, True) #c
        GPIO.output(12, False) #d
        GPIO.output(1, False) #e
        GPIO.output(7, True) #f
        GPIO.output(8, True) #g
    elif (number==5):
        GPIO.output(21, True) #a
        GPIO.output(20, False) #b
        GPIO.output(16, True) #c
        GPIO.output(12, True) #d
        GPIO.output(1, False) #e
        GPIO.output(7, True) #f
        GPIO.output(8, True) #g
    elif (number==6):
        GPIO.output(21, True) #a
        GPIO.output(20, False) #b
        GPIO.output(16, True) #c
        GPIO.output(12, True) #d
        GPIO.output(1, True) #e
        GPIO.output(7, True) #f
        GPIO.output(8, True) #g
    elif (number==7):
        GPIO.output(21, True) #a
        GPIO.output(20, True) #b
        GPIO.output(16, True) #c
        GPIO.output(12, False) #d
        GPIO.output(1, False) #e
        GPIO.output(7, False) #f
        GPIO.output(8, False) #g
    elif (number==8):
        GPIO.output(21, True) #a
        GPIO.output(20, True) #b
        GPIO.output(16, True) #c
        GPIO.output(12, True) #d
        GPIO.output(1, True) #e
        GPIO.output(7, True) #f
        GPIO.output(8, True) #g
    elif (number==9):
        GPIO.output(21, True) #a
        GPIO.output(20, True) #b
        GPIO.output(16, True) #c
        GPIO.output(12, True) #d
        GPIO.output(1, False) #e
        GPIO.output(7, True) #f
        GPIO.output(8, True) #g
def drawD2(number):
    if (number==0):
        GPIO.output(25, True) #a
        GPIO.output(24, True) #b
        GPIO.output(23, True) #c
        GPIO.output(18, True) #d
        GPIO.output(15, True) #e
        GPIO.output(14, True) #f
        GPIO.output(2, False) #g
    elif (number==1):
        GPIO.output(25, False) #a
        GPIO.output(24, True) #b
        GPIO.output(23, True) #c
        GPIO.output(18, False) #d
        GPIO.output(15, False) #e
        GPIO.output(14, False) #f
        GPIO.output(2, False) #g
    elif (number==2):
        GPIO.output(25, True) #a
        GPIO.output(24, True) #b
        GPIO.output(23, False) #c
        GPIO.output(18, True) #d
        GPIO.output(15, True) #e
        GPIO.output(14, False) #f
        GPIO.output(2, True) #g
    elif (number==3):
        GPIO.output(25, True) #a
        GPIO.output(24, True) #b
        GPIO.output(23, True) #c
        GPIO.output(18, True) #d
        GPIO.output(15, False) #e
        GPIO.output(14, False) #f
        GPIO.output(2, True) #g 
    elif (number==4):
        GPIO.output(25, False) #a
        GPIO.output(24, True) #b
        GPIO.output(23, True) #c
        GPIO.output(18, False) #d
        GPIO.output(15, False) #e
        GPIO.output(14, True) #f
        GPIO.output(2, True) #g
    elif (number==5):
        GPIO.output(25, True) #a
        GPIO.output(24, False) #b
        GPIO.output(23, True) #c
        GPIO.output(18, True) #d
        GPIO.output(15, False) #e
        GPIO.output(14, True) #f
        GPIO.output(2, True) #g
    elif (number==6):
        GPIO.output(25, True) #a
        GPIO.output(24, False) #b
        GPIO.output(23, True) #c
        GPIO.output(18, True) #d
        GPIO.output(15, True) #e
        GPIO.output(14, True) #f
        GPIO.output(2, True) #g
    elif (number==7):
        GPIO.output(25, True) #a
        GPIO.output(24, True) #b
        GPIO.output(23, True) #c
        GPIO.output(18, False) #d
        GPIO.output(15, False) #e
        GPIO.output(14, False) #f
        GPIO.output(2, False) #g
    elif (number==8):
        GPIO.output(25, True) #a
        GPIO.output(24, True) #b
        GPIO.output(23, True) #c
        GPIO.output(18, True) #d
        GPIO.output(15, True) #e
        GPIO.output(14, True) #f
        GPIO.output(2, True) #g
    elif (number==9):
        GPIO.output(25, True) #a
        GPIO.output(24, True) #b
        GPIO.output(23, True) #c
        GPIO.output(18, True) #d
        GPIO.output(15, False) #e
        GPIO.output(14, True) #f
        GPIO.output(2, True) #g
def drawD3(number):
    if (number==0):
        GPIO.output(3, True) #a
        GPIO.output(4, True) #b
        GPIO.output(17, True) #c
        GPIO.output(27, True) #d
        GPIO.output(22, True) #e
        GPIO.output(10, True) #f
        GPIO.output(9, False) #g
    elif (number==1):
        GPIO.output(3, False) #a
        GPIO.output(4, True) #b
        GPIO.output(17, True) #c
        GPIO.output(27, False) #d
        GPIO.output(22, False) #e
        GPIO.output(10, False) #f
        GPIO.output(9, False) #g
    elif (number==2):
        GPIO.output(3, True) #a
        GPIO.output(4, True) #b
        GPIO.output(17, False) #c
        GPIO.output(27, True) #d
        GPIO.output(22, True) #e
        GPIO.output(10, False) #f
        GPIO.output(9, True) #g
    elif (number==3):
        GPIO.output(3, True) #a
        GPIO.output(4, True) #b
        GPIO.output(17, True) #c
        GPIO.output(27, True) #d
        GPIO.output(22, False) #e
        GPIO.output(10, False) #f
        GPIO.output(9, True) #g 
    elif (number==4):
        GPIO.output(3, False) #a
        GPIO.output(4, True) #b
        GPIO.output(17, True) #c
        GPIO.output(27, False) #d
        GPIO.output(22, False) #e
        GPIO.output(10, True) #f
        GPIO.output(9, True) #g
    elif (number==5):
        GPIO.output(3, True) #a
        GPIO.output(4, False) #b
        GPIO.output(17, True) #c
        GPIO.output(27, True) #d
        GPIO.output(22, False) #e
        GPIO.output(10, True) #f
        GPIO.output(9, True) #g
    elif (number==6):
        GPIO.output(3, True) #a
        GPIO.output(4, False) #b
        GPIO.output(17, True) #c
        GPIO.output(27, True) #d
        GPIO.output(22, True) #e
        GPIO.output(10, True) #f
        GPIO.output(9, True) #g
    elif (number==7):
        GPIO.output(3, True) #a
        GPIO.output(4, True) #b
        GPIO.output(17, True) #c
        GPIO.output(27, False) #d
        GPIO.output(22, False) #e
        GPIO.output(10, False) #f
        GPIO.output(9, False) #g
    elif (number==8):
        GPIO.output(3, True) #a
        GPIO.output(4, True) #b
        GPIO.output(17, True) #c
        GPIO.output(27, True) #d
        GPIO.output(22, True) #e
        GPIO.output(10, True) #f
        GPIO.output(9, True) #g
    elif (number==9):
        GPIO.output(3, True) #a
        GPIO.output(4, True) #b
        GPIO.output(17, True) #c
        GPIO.output(27, True) #d
        GPIO.output(22, False) #e
        GPIO.output(10, True) #f
        GPIO.output(9, True) #g
#global var to reresh get data
requestAPI = True
UUID = "ninguno"
def setGlobal(val):
    global UUID    # Needed to modify global copy of globvar
    UUID = val
def showDisplays():
    lastRegistre = requests.get("https://xqgua01dfk.execute-api.us-east-2.amazonaws.com/GetData/getdata")
    lastRegistreResponse = json.loads(lastRegistre.text)

    requestAPI = False if (UUID == str(lastRegistreResponse['Body']['UUID'])) else True
    if (requestAPI == True):
        setGlobal(str(lastRegistreResponse['Body']['UUID']))
        
    OperationResult =lastRegistreResponse['Body']['OperationResult']
    NumberParts = OperationResult.split(".")
    #turn of points
    GPIO.output(0, False)
    GPIO.output(11, False)
    if(int(NumberParts[0]) > 99):
        #display 1
        drawD1(int(NumberParts[0][0]))
        #display 2
        drawD2(int(NumberParts[0][1]))
        #display 3
        drawD3(int(NumberParts[0][2]))
         
    elif(int(NumberParts[0]) > 9):
        #display 1
        drawD1(int(NumberParts[0][0]))
        #punto display 2
        GPIO.output(11, True)  
        #display 2
        drawD2(int(NumberParts[0][1]))
        #display 3
        drawD3(int(NumberParts[1][0]))
    else:
        #display 1
        drawD1(int(NumberParts[0][0]))
        #punto display 1
        GPIO.output(0, True)   
        #display 2
        drawD2(int(NumberParts[1][0]))
        #display 3
        drawD3(int(NumberParts[1][1]))
 
def writeData(contador, operacion):
    x = {
        "Request": "insert",
        "contador": int(contador),
        "operacion": operacion,
        "dispositivo": "Raspberry"
    }
    r = requests.post(url = API_ENDPOINT, data = json.dumps(x))
    response = json.loads(r.text)
    display =response['display']
    print(str(display))
tiempoInicio = datetime.now()#obtener fecha y hora
while True:
    tiempo = datetime.now()
    #determinar operacion a realizar
    operacion = ''
    operacion += '1' if GPIO.input(19) else'0'
    operacion += '1' if GPIO.input(13) else'0'
    operacion += '1' if GPIO.input(6) else'0'
    operacion += '1' if GPIO.input(5) else'0'
    showDisplays()

    if ((contador > 14) or (abs(tiempo.second - tiempoInicio.second) > 10)): #verificacion de interrupciones o exceso de tiempo
        if(requestAPI):
            requestAPI = False
            writeData(contador, operacion) #post data endpoint
        contador = 0 #reinicio de contador
        tiempoInicio = datetime.now()
    if not GPIO.input(26): #gpio 20 entrada
        contador +=1 #deteccion de interrupcion
        requestAPI = True
        print("Se ha detectado una interrupcion "+str(contador)+ " interrupciones totales.")