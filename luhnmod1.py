#!/usr/bin/env python
#-*- coding:utf-8 -*-

import random
import os

#vars
prpan = []
validcc = []

def algoth(bin):
	#funcvars
	prpan = []
	ibin = bin
	pan = ''
	nrnd1 = random.randint(0,9)
	check = random.randint(0,9) #ultimo digito del pan
	iai = random.randint(0, 999999999) #9 digitos generados aleatoreamente
	striai = str(iai) #almacenados en una nueva variable pero ahora en formato string 
	strcheck = str(check)
	pan = ibin + striai + strcheck
	if(len(pan) <= 15):
		pan = ibin + striai + str(nrnd1) + strcheck
		#return pan
	#fase1 : elevar cada segundo nro desde la derecha, sumar por separado nros > 10, Ej 10 = 1 + 0 = 1
	contnum = 0
	for num in pan:
		sum = 0
		if(contnum%2 != 0):
			prpan.append(num)
		if(contnum%2 == 0):
			sum = int(num) + int(num)
			if(sum >= 10):
				strsum = str(sum)
				dgt1 = strsum[0]
				dgt2 = strsum[1]
				sum = int(dgt1) + int(dgt2)
			prpan.append(sum)
		contnum +=1
	#fase2 : sumar todos los nros para analizar si sum%10 ?= 0 
	newpan = prpan
	sum = 0
	try:
		for p in newpan:
			if(p == ' '):
				p = ''
			sum += int(p)
	except ValueError:
		cnte = 0
		e = ValueError
		cnte += 1
	if(sum%10 == 0):
		validcc.append(pan)
		for cc in validcc:
			print("[0]ok|[1]bad>"+str(sum%10))
			print(cc)
			print("$#bin#$")
			os.system('sudo grep -i '+cc[0:6]+' data/binlist')
			print("$~$~$~$~$~$~$~-~$-~$~$~$~$~$")
	if(sum%10 != 0):
		pass
	#--


