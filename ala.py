#!/usr/bin/ env python
#-*- coding:utf-8 -*-
#TO DO
# agregar filtros para que muestre busquedas especificas
#Autor Carlos a r Mago & Fr33 Coders Gpl v3

import os
import random
import argparse
from luhnmod1 import algoth
#Vars
file = open('data/binlist')
run = True
binlist = []
namelist = []
surnamelist = []
pan = ''

parser = argparse.ArgumentParser(
	prog = 'ala.py',
	description = 'analiza el bin guardado en el archivo binlist para generar nros  luhn\'s ',
	epilog = '[Analizador] [L]uhn [A]lgoritmo'
	)
parser.add_argument('--todos', action='store_true', help='Extrae todas las lineas de bin list para generar nros luhn\'s')
parser.add_argument('--cantidad', action='store_true', help='Extrae la cantidad seleccionada para mostrar nros luh\'s aleatorios')
##Extrae los primeros 8 caracteres del archivo binlist
def genvalidcc(file):
	e = 0
	#por cada linea en el texto evitando los caracteres que no sean digitos con la excepcion de ValueError
	for l in file:
		try:
			bnum = file.readline()[0:6]
			intbnum = int(bnum)
			#evitamos que nuestros 6 digitos esten libre de cualquier otro caracter
			if(bnum == ' ' or bnum == '-' or bnum == '*' or bnum == 'x' or bnum == '['):
				bnum = ''
				binlist.append(bnum)
			if(len(bnum) > 5):
				binlist.append(bnum)
		except ValueError:
			e += 1
	#pasa los nros al modulo para generar un pan(primary account number)

#-- - -
if(__name__ == '__main__'):
	genvalidcc(file)
	args = parser.parse_args()
	if(args.todos == True):
		for bin in binlist:
			pan = algoth(bin)
	if(args.cantidad == True):
		contop2 = 0
		opcant = input('cantidad > ')
		for bin in binlist:
			pan = algoth(bin)
			contop2 += 1
			if(contop2 >= int(opcant)):
				break
	
