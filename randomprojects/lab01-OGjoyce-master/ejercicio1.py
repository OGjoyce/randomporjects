# -*- coding: utf-8 -*-
import sys

''' Escriba aqui en orden de arriba a abajo, los 5 numeros que forman
	la leta "A" en la primer respuesta del primer inciso ejercicio 1
	Q = ¿Cuáles 5 números decimales producen el patrón de la letra "A" mostrada arriba?
'''
I1_R1 = 0110
I1_R2 = 1001
I1_R3 = 1111
I1_R4 = 1001
I1_R5 = 1001

'''	Escriba aqui en orden de arriba a abajo, los 5 numeros en representacion
	hexadecimal que forman la letra "A" en la segunda respuesta 
	primer inciso del ejercicio 1
	Ingreselos como String
	Q = ¿Cuales 5 números hexadecimales?
'''
I1_R6 = "6"
I1_R7 = "9"
I1_R8 = "D"
I1_R9 = "9"
I1_R10 = "9"

'''	Escriba aqui la letra que se forma con los numeros 1,1,9,9,6 escritos de 
	arriba hacia abajo en el en la primer respuesta del segundo inciso del ejercicio 1
	Q = ¿Que letra se dibuja con 1, 1, 9, 9, 6?
'''
I2_R1 = "J"

'''	Escriba aqui la letra que se forma con los numeros 0xF8F88 escritos de 
	arriba hacia abajo en la segunda respuesta del segundo inciso del ejercicio 1
	Q = ¿Con 0xF8F88?
'''
I2_R2 = "F"

'''	Escriba aqui, en forma hex, que numero utilizaria para 
	repentar la letra S en la primer respuesta del tercer inciso del ejercicio 1
	Q = ¿Qué representación hexadecimal usarían para dibujar la letra S?
'''
I3_R1 = "0xC864E"

'''	Escriba aqui, en forma hex, que numero utilizaria para 
	repentar la letra D en la segunda respuesta del tercer inciso del ejercicio 1
	Q = ¿Qué representación hexadecimal usarían para dibujar la letra D?
'''
I3_R2 = "0xE999E"

#No to que nada a partir de este codigo#
def formatH(string):
	return string.replace("0X","").replace("0x","")

def main(option):
	if option == 1 :
		print str(I1_R1)+";"+str(I1_R2)+";"+str(I1_R3)+";"+str(I1_R4)+";"+str(I1_R5)
	elif option == 2:
		print formatH(I1_R6)+";"+formatH(I1_R7)+";"+formatH(I1_R8)+";"+formatH(I1_R9)+";"+formatH(I1_R10)
	elif option == 3:
		print I2_R1
	elif option == 4:
		print I2_R2
	elif option == 5:
		print formatH(I3_R1)
	elif option == 6:
		print formatH(I3_R2)
	else:
		print "Opcion Invalida"


if __name__ == "__main__":
	if len(sys.argv) == 2:
		main(int(sys.argv[1]))
	else:
		print "parametros incorrectos"
