#!/usr/bin/python
# -*- coding: utf-8 -*-

#Para este ejercicio usamos una librería lamada "numpy", para Kubuntu 14,04, con python 2.7.6
#apt-get install python-numpy

import numpy as lr #comando lr.shape(Matriz)
from sympy import *

def m_cuadrada(xx,z):
  print "Ingresa a método"
  #condiciones iniciales de las 2 caras cuadradas
  #xx será lado caras (xx, xx) "cuadrada"
  #z será profundidad del paralelepípedo
  #La matriz creada será de la Forma prl[z][y][x] con los siguientes valores en los bordes externos de la matriz
  h = 0.999999999999	#condicion de temperaturas
  R = 12	#temperatura refrigerante
  A = h*(0 - R)	#condicion Cara Aislante
  B = h*(60 - R)	#condicion 4
  
  dx2=1/9
  dy2=1/3
  dz2=1/4
  print "Asigna valores"
  #Validar dx2, dy2 ,dz2 con valores 0 < dx2, dy2 ,dz2 <1
  
  AL = xx*dx2
  P = z*dz2
  
  #Realiza las particiones necesarias para las diferencias divididas de cada nodo en la matriz
  
  prl = [[["" for x in xrange(P)] for x in xrange(AL)] for x in xrange(AL)]
  
  #def iz_up(x,y,dd):	# x=nodo anterior	y=contorno	dd=diferencia
  #return (x-2*dd*h*(x-y))
  print "inicia 1er FOR"

  for i in range(0,P):		#rellenado condiciones de borde
    print "Valor de i={} primer for".format(i)
    for j in range(0,AL):
      print "Valor de j{}".format(j)
      prl[i][0][j] = R
      prl[i][AL-1][j] = R
      prl[i][j][0] = R
      prl[i][j][AL-1] = R
  print prl
  
  print "inicia 2º FOR"
  for i in range(0,AL):		#Rellenando condiciones en caras
    print "Valor de i={} segundo for".format(i)
    for j in range(0,AL):
      print "Valor de j{}".format(j)
      prl[0][i][j] = A
      prl[P-1][i][j] = B
  
  print prl
  
  print "inicia 3er FOR"
  in_nd = 0
  for i in range(1,P-1):		#relleno con las variables "symbolic" a nodos equisdistantes
    print "Valor de i={} tercer for".format(i)
    for j in range(1,AL-1):		#por dentro de la superficie
      print "Valor de j{}".format(j)
      for k in range(1,AL-1):
	print "Valor de k{}".format(k)
	nd = "T"+str(in_nd)
	sy = symbolics(nd)
	prl[i][j][k] = sy
	in_nd += 1		#numerará los nodos uno x uno hasta terminar cada celda de la matriz
  
  print prl
#Matriz llena con valores T0 hasta T(in_nd)

xx =input("Ingrese Valor de Lado: ")
z =input("Ingrese Valor de profundidad: ")

m_cuadrada(xx,z)
  

  
