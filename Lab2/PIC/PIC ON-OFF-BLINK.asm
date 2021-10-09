;CONFIGURACIÓN INICIAL
	ORG 0X00
	GOTO START
START
	BSF STATUS, 5
	CLRF TRISB      ;limpiezas
	CLRF TRISC
	CLRF TRISD
	BSF TRISC,0     ;configurar como input
	BSF TRISC,1     ;configurar como input
	BCF STATUS, 5
	CALL PRINCIPAL  ;llamada a principal para comparaciones
    GOTO 	START   ;volver a start

PRINCIPAL
    BTFSS	PORTC,1 ;si el puerto 1 de c no viene se llama a turn para encender
    CALL    TURN    
    BTFSC	PORTC,1 ;si el puerto 1 de c viene, se llama a blink
	CALL 	BLINK	
	RETURN

BLINK
    CALL TURNON     ;blink, enciende y apaga puerbo b
    CALL TURNOFF
    RETURN

TURN
    BTFSC	PORTC,0 ;el puerto b debe encenderse si viene 0 de c
	CALL 	TURNON	
	BTFSS	PORTC,0 ;el puerto b debe apagarse si viene 0 de c
	CALL 	TURNOFF	
    RETURN
TURNON
    MOVLW B'11111111'
	MOVWF PORTB     ;se enciende el puerto
    RETURN
TURNOFF
    MOVLW B'00000000'
	MOVWF PORTB     ;se apaga el puerto
    RETURN

END