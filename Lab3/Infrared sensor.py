from datetime import datetime
import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.OUT) #set pin de salida
GPIO.setup(20, GPIO.IN) #set pin de entrada
interrupciones = 0 #variable para interrupciones del sensor
GPIO.output(21, False) #reset del pin para que arranque en 0
while True:
    tiempo = datetime.now()#obtener fecha y hora
    
    if (interrupciones > 4): #verificacion de interrupciones para encender led
        GPIO.output(21, True)
        
    if GPIO.input(20): #gpio 20 entrada
        print("Se ha detectado una continuidad de sensor a las " + str(tiempo)+ " se han registrado: "+str(interrupciones) +" interrupciones.")
        while GPIO.input(20):
            tiempo = datetime.now()
    else:
        interrupciones +=1 #deteccion de interrupcion
        print("Se ha detectado una interrupcion de sensor a las " + str(tiempo) + " se han registrado: "+str(interrupciones)+ " interrupciones.")
        while not GPIO.input(20):
            tiempo = datetime.now()
        
GPIO.cleanup()
