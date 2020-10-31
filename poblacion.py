import os
import time
os.environ.setdefault("DJANGO_SETTINGS_MODULE","reporte_django_2.settings")
import django, random as ran
from random import random

django.setup()

from datos.models import Datos

vocales = ['a','e','i','o','u','A','E','I','O','U']
consonantes = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','x','y','z',
				'B','C','D','F','G','H','J','K','L','M','N','P','Q','R','S','T','V','X','Y','Z']


def generar_cadena(length):
	if length <= 0:
		return False

	cadena = ''

	for i in range(length):
		decision = ran.choice(('consonantes','vocales'))

		if cadena[-1:].lower() in vocales:
			decision = 'consonantes'
		if cadena[-1:].lower() in consonantes:
			decision = 'vocales'

		if decision == 'consonantes':
			op_letra = ran.choice(consonantes)
		else:
			op_letra = ran.choice(vocales)

		if cadena == '':
			cadena += op_letra.upper()
		else:
			cadena += op_letra

	return cadena

def generar_numero():
	numero = int(random()*10+1)
	return numero


def poblacion(tama):
	for i in range(tama):
		length = ran.randint(2,20)
		nom = generar_cadena(length)
		edad = generar_numero()
		ape = generar_cadena(length)
		direc = generar_cadena(length)
		dato = Datos.objects.get_or_create(nombre = nom, edad = edad, apellidos = ape, direccion = direc)[0]
		dato.save()

		print("Iteración Nº :"+str(i))


if __name__ == '__main__':
	print("Creando población . . Por favor espere :D")
	inicio = time.strftime("%c")
	print("Fecha y hora de inicio: "+time.strftime("%c"))
	poblacion(10)
	fin = time.strftime("%c")
	print("Fecha y hora de inicio: "+time.strftime("%c"))
	print("Inicio: "+str(inicio)+" - Fin: "+str(fin))
	print("Población completa!! :D")
