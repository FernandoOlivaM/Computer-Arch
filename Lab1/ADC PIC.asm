; José Fernando Oliva Morales 1251518
; CONFIGUTACION
; el puerto c es para el ADC
; el puerto d es para el dispaly
; el puerto b es para el resultado binario de la suma
	ORG	0X00
	GOTO	INCIO

; INCIO
INCIO

    BCF     STATUS, 5
    BCF     STATUS, 6

    MOVLW   B'01000001' ;ADC on
    MOVWF   ADCON0

    BSF     STATUS, 5
    BCF     STATUS, 6

    CLRF    TRISA  ;limpiezas
	CLRF	TRISB
    CLRF    TRISC
    CLRF    TRISD
    CLRF    TRISE

    MOVLW   B'00000111'
    MOVWF   OPTION_REG

    MOVLW   B'00001110'
    MOVWF   ADCON1

    BSF     TRISA, 0	;trist para leer adc

    BCF     STATUS, 5
    BCF     STATUS, 6

LOOP
    BTFSS   INTCON, T0IF
    GOTO 	LOOP
    BCF     INTCON, T0IF
    BSF     ADCON0, GO
ESPERA
    BTFSC   ADCON0, GO  ;esperar para leer el valor del adc
    GOTO 	ESPERA
    MOVF    ADRESH, W
    MOVWF   PORTC
	MOVF 	ADRESL, W
	MOVWF 	PORTD 		
	CALL 	LECTURA
    GOTO 	LOOP

LECTURA
	BTFSC	PORTC,7
	CALL 	COMPARA2	;el primer bit es 1
	BTFSS	PORTC,7
	CALL 	COMPARA1	;el pimer bit es 0
	RETURN
;los COMPARA representan la intensidad de la luz
COMPARA1;0-7
	BTFSC	PORTC,6
	CALL 	COMPARA3
	BTFSS	PORTC,6
	CALL 	COMPARA4
	RETURN

COMPARA2 ;8 Y 9
	BTFSC	PORTC,4
	CALL 	NUEVE
	BTFSS	PORTC,4
	CALL 	OCHO
	RETURN

COMPARA3 ;4-7
	BTFSC	PORTC,5
	CALL 	COMPARA8
	BTFSS	PORTC,5
	CALL 	COMPARA7
	RETURN

COMPARA4;0-3
	BTFSC	PORTC,5
	CALL 	COMPARA6
	BTFSS	PORTC,5
	CALL 	COMPARA5
	RETURN

COMPARA5;0-1
	BTFSC	PORTC,4
	CALL 	UNO
	BTFSS	PORTC,4
	CALL 	CERO
	RETURN

COMPARA6; 2-3
	BTFSC	PORTC,4
	CALL 	TRES
	BTFSS	PORTC,4
	CALL 	DOS
	RETURN

COMPARA7 ;4-5
	BTFSC	PORTC,4
	CALL 	CINCO
	BTFSS	PORTC,4
	CALL 	CUATRO
	RETURN


COMPARA8 ;6-7
	BTFSC	PORTC,4
	CALL 	SIETE
	BTFSS	PORTC,4
	CALL 	SEIS
	RETURN


CERO
	MOVLW	B'11111111' ; se encienden todos

	MOVWF	PORTD
	BCF		PORTD, 6 	; se apaga el segmento g
    ;suma
    CLRW ;limpieza
    ADDLW   d'5' ;sumando 5
    MOVWF	PORTB ;mostrando resultado suma en puerto b
	RETURN

UNO
	MOVLW	0X00
	MOVWF	PORTD
	BSF		PORTD, 1 ;enciende segmento b
	BSF		PORTD, 2 ;enciende segmento c
    ;suma
    CLRW ;limpieza
    ADDLW   d'1' ;sumando 1
    ADDLW   d'3' ;sumando 3
    MOVWF	PORTB ;mostrando resultado suma en puerto b
	RETURN

DOS
	MOVLW	0X00
	MOVWF	PORTD
	BSF		PORTD, 4	;enciende segmento e
	BSF		PORTD, 3	;enciende segmento d
	BSF		PORTD, 1	;enciende segmento b
	BSF		PORTD, 6	;enciende segmento g
	BSF		PORTD, 0	;enciende segmento a
    ;suma
    CLRW ;limpieza
    ADDLW   d'2' ;sumando 2
    ADDLW   d'6' ;sumando 6
    MOVWF	PORTB ;mostrando resultado suma en puerto b
	RETURN

TRES
	MOVLW	0X00
	MOVWF	PORTD
	BSF		PORTD, 3	 ;enciende segmento d
	BSF		PORTD, 2	 ;enciende segmento c
	BSF		PORTD, 1	 ;enciende segmento b
	BSF		PORTD, 6	 ;enciende segmento g
	BSF		PORTD, 0	 ;enciende segmento a
    ;suma
    CLRW ;limpieza
    ADDLW   d'3' ;sumando 3
    ADDLW   d'8' ;sumando 8
    MOVWF	PORTB ;mostrando resultado suma en puerto b
	RETURN

CUATRO
	MOVLW	0X00
	MOVWF	PORTD
	BSF		PORTD, 2	 ;enciende segmento c
	BSF		PORTD, 1	 ;enciende segmento b
	BSF		PORTD, 6	 ;enciende segmento g
	BSF		PORTD, 5	 ;enciende segmento f
    ;suma
    CLRW 				 ;limpieza
    ADDLW   d'4' 		 ;sumando 4
    ADDLW   d'2' 		 ;sumando 2
    MOVWF	PORTB 			;mostrando resultado suma en puerto b
	RETURN

CINCO
	MOVLW	0X00
	MOVWF	PORTD
	BSF		PORTD, 3	 ;enciende segmento d
	BSF		PORTD, 2	 ;enciende segmento c
	BSF		PORTD, 6	 ;enciende segmento g
	BSF		PORTD, 5	 ;enciende segmento f
	BSF		PORTD, 0	 ;enciende segmento a
    ;suma
    CLRW ;limpieza
    ADDLW   d'5' ;sumando 5
    ADDLW   d'4' ;sumando 4
    MOVWF	PORTB ;mostrando resultado suma en puerto b
	RETURN

SEIS
	MOVLW	0X00
	MOVWF	PORTD
	BSF		PORTD, 4	 ;enciende segmento e
	BSF		PORTD, 3	 ;enciende segmento d
	BSF		PORTD, 2	 ;enciende segmento c
	BSF		PORTD, 6	 ;enciende segmento g
	BSF		PORTD, 5	 ;enciende segmento f
	BSF		PORTD, 0	 ;enciende segmento a
    ;suma
    CLRW ;limpieza
    ADDLW   d'6' ;sumando 6
    ADDLW   d'7' ;sumando 7
    MOVWF	PORTB ;mostrando resultado suma en puerto b
	RETURN

SIETE
	MOVLW	0X00
	MOVWF	PORTD
	BSF		PORTD, 1    ;enciende segmento b
	BSF		PORTD, 2    ;enciende segmento c
	BSF		PORTD, 0    ;enciende segmento a
    ;suma
    CLRW ;limpieza
    ADDLW   d'7' ;sumando 7
    ADDLW   d'0' ;sumando 0
    MOVWF	PORTB ;mostrando resultado suma en puerto b
	RETURN

OCHO
	MOVLW	B'11111111' ;encienden todos los segmentos
	MOVWF	PORTD
    ;suma
    CLRW ;limpieza
    ADDLW   d'8' ;sumando 8
    ADDLW   d'4' ;sumando 4
    MOVWF	PORTB ;mostrando resultado suma en puerto b
	RETURN

NUEVE
	MOVLW	0X00
	MOVWF	PORTD
    BSF		PORTD, 3	 ;enciende segmento d
	BSF		PORTD, 2	 ;enciende segmento c
	BSF		PORTD, 1	 ;enciende segmento b
	BSF		PORTD, 6	 ;enciende segmento g
	BSF		PORTD, 5	 ;enciende segmento f
	BSF		PORTD, 0	 ;enciende segmento a
    ;suma
    CLRW ;limpieza
    ADDLW   d'9' ;sumando 9
    ADDLW   d'5' ;sumando 5
    MOVWF	PORTB ;mostrando resultado suma en puerto b
	RETURN
END