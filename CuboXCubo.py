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
  
  for k in range (0,z):		#Primera opción de código
    for i in range(0,xx):	#largo
      for j in range(0,xx):	#ancho
	if k==0:
	  #aislante
	  if (i>0 and i<xx-1) and (j==0 or j<xx-1):
	    prl[k][i][j] = R	#Borde cara
	  elif i>0 or i<xx-1 or j>0 or j<xx-1:
	    prl[k][i][j] = A	#Interior cara
	    
	elif k==z-1:
	  #zona caliente
	  if i=0 or i==xx-1 or j=0 or j == xx-1:
	    prl[k][i][j] = R	#Borde cara
	  elif i>0 or i<xx-1 or j>0 or j<xx-1:
	    prl[k][i][j] = C	#Interior cara
	elif k>0 and k<z-1:
	  #rellenando borde material conductivo
	  if i=0 or i==xx-1 or j=0 or j == xx-1:
	    prl[k][i][j] = R	#Borde cara
	  elif i>0 or i<xx-1 or j>0 or j<xx-1:
	    prl[k][i][j] = C	#Interior cara
  
  
  

xx =input("Ingrese Valor de Lado: ")
z =input("Ingrese Valor de profundidad: ")

m_cuadrada(xx,z)
  
  
  
  
  
	
  
  
  
