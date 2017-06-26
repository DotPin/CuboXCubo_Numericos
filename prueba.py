#!/usr/bin/python
# -*- coding: utf-8 -*-

from sympy import *

h = 0.999999999999	#condicion de temperaturas
R = 12	#temperatura refrigerante
A = h*(0 - R)	#condicion Cara Aislante
B = h*(60 - R)	#condicion 4

dx = 0.25
dy = 0.1
dz = 0.5

xx=4
xy=4
z=5

#xx= int(round(xx/dx))		#dx dy dz son variaciones dif_finitias del nodo para calcular dimensiones correctas de la matriz 3D
#xy = int(round(xy/dy))		#las deja en entero para poder generar la matriz 3D
#z= int(round(z/dz))

prl = [[["" for x in xrange(xx)] for x in xrange(xx)] for x in xrange(z)]

for i in range(0,z):		#rellenado condiciones de borde
    for j in range(0,xx):
      prl[i][0][j] = R
      prl[i][xx-1][j] = R
      prl[i][j][0] = R
      prl[i][j][xx-1] = R
      
for i in range(0,xx):		#Rellenando condiciones en caras
  for j in range(0,x):
    prl[0][i][j] = A
    prl[z-1][i][j] = B

in_nd = 0
for i in range(1,z-1):		#relleno con las variables "symbolic" a nodos equisdistantes
  print "Cara {}".format(i)
  for j in range(1,xx-1):		#por dentro de la superficie
    for k in range(1,xx-1):
      nd = "T"+str(in_nd)
      sy = symbols(nd)
      #prl[z][y][x]
      prl[i][j][k] = sy
      print "{}".format(prl[i][j][k])
      in_nd += 1		#numerará los nodos uno x uno hasta terminar cada celda de la matriz	
    
print "************************Mostrando Matriz******************************"

for i in range(0,z):		#relleno con las variables "symbolic" a nodos equisdistantes
  print "Cara {}".format(i)
  for j in range(0,xx):		#por dentro de la superficie
    for k in range(0,xx):
      print prl[i][j][k],
      #print "{} \t".format(prl[i][j][k])
      in_nd += 1
    print "\n"

    
w = ["" for x in range(xx*z*xx)]
      
#x = ["" for x in range(xx*z)] generar vector para generar matriz H[x*y*z] y rellenar con ecuación elíptica de nodos
#despues generar matriz con datos de tipo A[x*y*z,x*y*z] y vector B[x*y*z] a incógnitas de tipo Ax=B