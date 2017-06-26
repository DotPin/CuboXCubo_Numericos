#!/usr/bin/python
# -*- coding: utf-8 -*-

#Para este ejercicio usamos una librería lamada "numpy", para Kubuntu 14,04, con python 2.7.6
#apt-get install python-numpy

import numpy as lr #comando lr.shape(Matriz)
from sympy import *

def m_cuadrada(xx,z):
  #condiciones iniciales de las 2 caras cuadradas
  #xx será lado caras (xx, xx) "cuadrada"
  #z será profundidad del paralelepípedo
  #La matriz creada será de la Forma prl[z][y][x] con los siguientes valores en los bordes externos de la matriz
  h = 0.999999999999	#condicion de temperaturas
  R = 12	#temperatura refrigerante
  A = h*(0 - R)	#condicion Cara Aislante
  C = h*(60 - R)	#condicion 4
  
  dx2=1/9
  dy2=1/3
  dz2=1/4
  #Validar dx2, dy2 ,dz2 con valores 0 < dx2, dy2 ,dz2 <1
  
  AL = xx*dx2
  P = dz2*z
  
  #Realiza las particiones necesarias para las diferencias divididas de cada nodo en la matriz
  
  prl = [[["" for x in xrange(P)] for x in xrange(AL)] for x in xrange(AL)]
  
  #def iz_up(x,y,dd):	# x=nodo anterior	y=contorno	dd=diferencia
  #return (x-2*dd*h*(x-y))

  for i in range(0,P):		#rellenado condiciones de borde
    for j in range(0,AL):
      prl[i][0][j] = R
      prl[i][AL-1][j] = R
      prl[i][j][0] = R
      prl[i][j][AL-1] = R
  print prl

  for i in range(0,AL):		#Rellenando condiciones en caras
    for j in range(0,AL):
      prl[0][i][j] = A
      prl[P-1][i][j] = B
  
  print prl
  
  in_nd = 0
  for i in range(1,P-1):		#relleno con las variables "symbolic" a nodos equisdistantes
    for j in range(1,AL-1):		#por dentro de la superficie
      for k in range(1,AL-1):
	nd = "T"+str(in_nd)
	sy = symbolics(nd)
	prl[i][j][k] = sy
	in_nd += 1		#numerará los nodos uno x uno hasta terminar cada celda de la matriz
  
  print prl
#Matriz llena con valores T0 hasta T(in_nd)

xx =input("Ingrese Valor de Lado: ")
z =input("Ingrese Valor de profundidad: ")

m_cuadrada(xx,z)
  
  
  
  
  #for k in range (0,z):		#Primera opción de código
    #for i in range(0,xx):	#largo
      #for j in range(0,xx):	#ancho
	#if k==0:
	  ##aislante
	  #if (i>0 and i<xx-1) and (j==0 or j<xx-1):
	    #prl[k][i][j] = R	#Borde cara
	  #elif i>0 or i<xx-1 or j>0 or j<xx-1:
	    #prl[k][i][j] = A	#Interior cara
	    
	#elif k==z-1:
	  ##zona caliente
	  #if i=0 or i==xx-1 or j=0 or j == xx-1:
	    #prl[k][i][j] = R	#Borde cara
	  #elif i>0 or i<xx-1 or j>0 or j<xx-1:
	    #prl[k][i][j] = C	#Interior cara
	#elif k>0 and k<z-1:
	  ##rellenando borde material conductivo
	  #if i=0 or i==xx-1 or j=0 or j == xx-1:
	    #prl[k][i][j] = R	#Borde cara
	  #elif i>0 or i<xx-1 or j>0 or j<xx-1:
	    #prl[k][i][j] = C	#Interior cara
	
  
  
  
