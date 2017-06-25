#Para este ejercicio usamos una librería lamada "numpy", para Kubuntu 14,04, con python 2.7.6
#apt-get install python-numpy

import numpy as lr #comando lr.shape(Matriz)
from random import rnd

def m_cuadrada(xy,z):
  prl = [[["" for x in xrange(xy)] for x in xrange(xy)] for x in xrange(z)]
  #condiciones iniciales de las 2 caras cuadradas
  #xx será lado caras (xx, xx) "cuadrada"
  #z será profundidad del paralelepípedo
  #La matriz creada será de la Forma prl[z][xx][xx] con los siguientes valores en los bordes externos de la matriz
  h = 0.999999999999	#condicion de temperaturas
  R = 12	#temperatura refrigerante
  A = h*(0-r)	#condicion Cara Aislante
  C = h*(60-r)	#condicion 4
  
  dx2=
  dy2=
  dz2=
  
  def iz_up(x,y,dd):	# x=nodo anterior	y=contorno	dd=diferencia
  return (x-2*dd*h*(x-y))

  
  
  
  
  
  for k in range (0,z):		#capa
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
	
  
  
  
