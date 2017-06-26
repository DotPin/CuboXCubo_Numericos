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

xx=3
xy=4
z=6

xx= int(round(xx/dx))
xy = int(round(xy/dy))
z= int(round(z/dz))

prl = [[["" for x in xrange(xx)] for x in xrange(xx)] for x in xrange(z)]

for i in range(0,z):		#rellenado condiciones de borde
    print "Valor de i={} primer for".format(i)
    for j in range(0,xx):
      print "Valor de j{}".format(j)
      prl[i][0][j] = R
      prl[i][xx-1][j] = R
      prl[i][j][0] = R
      prl[i][j][xx-1] = R
    print prl
  
for i in range(0,xx):		#Rellenando condiciones en caras
  print "Valor de i={} segundo for".format(i)
  for j in range(0,x):
    print "Valor de j{}".format(j)
    prl[0][i][j] = A
    prl[z-1][i][j] = B

in_nd = 0
for i in range(1,z-1):		#relleno con las variables "symbolic" a nodos equisdistantes
  print "print i {}".format(i)
  for j in range(1,xx-1):		#por dentro de la superficie
    print "print j {}".format(j)
    for k in range(1,xx-1):
      print "print k {}".format(k)
      nd = "T"+str(in_nd)
      sy = symbols(nd)
      #prl[z][y][x]
      prl[i][j][k] = sy
      print prl
      in_nd += 1		#numerará los nodos uno x uno hasta terminar cada celda de la matriz
      
