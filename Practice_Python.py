#!/usr/bin/python2.7

#Calculo del volumen de una esfera donde r es una variable

a=4.0
b=3.0
cons=a/b
import math
pi= math.pi
r=3

volesf= cons*pi*r**3

print volesf


def volume(radio):
	vol= cons*pi*radio**3
	return vol

radius= volume(3)
print radius

#Usando Strings: dos ejercicios



p= "Universidad de los Andes"
u= p[0:11]
n= p[19:24]

print u
print n



lista= list(range(3,16,3))
print lista



#Usando Diccionarios

d= dict()
d[1] = "Enero"
d[12] = "Diciembre"
d[3] = "Marzo"


d[4] = "Abril"
d[5] = "Mayo"


del d[1]
print d



#Iteracion con bucle de for

nombres=[ 'Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo']



#Control de Flujo

def vocales(cadena):
	vocal=0
	for letra in cadena:
		if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u' or letra == 'A' or letra == 'E' or letra == 'I' or letra == 'O' or letra == 'U':
			vocal=vocal+1
	return vocal
cadena = raw_input('')
print vocales(cadena)



#Funciones



#Objetos

class rectangulo():
	def __init__(self, a=1.0, b=2.0):
		self.a = a
		self.b = b
		self.__area = a * b
	def set_area(self):
		self.__area = self.a * self.b
	def print_object(self):
		print("a", self.a)
		print("b", self.b)
		print("area", self.__area)

A = rectangulo()
A.print_object()

A.z =5.0
A.print_object()

A._area = 18.0
A.print_object()

A.set_area()
A.print_object()







