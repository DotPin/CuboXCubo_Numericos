#!/usr/bin/python
# -*- coding: utf-8 -*-

from sympy import *

xx=3
xy = 4
z=5

prl = [[["" for x in xrange(xx)] for x in xrange(xy)] for x in xrange(z)]

in_nd = 0
for i in range(0,z):		#relleno con las variables "symbolic" a nodos equisdistantes
  print "print i {}".format(i)
  for j in range(0,xy):		#por dentro de la superficie
    print "print j {}".format(j)
    for k in range(0,xx):
      print "print k {}".format(k)
      nd = "T"+str(in_nd)
      sy = symbols(nd)
      #prl[z][y][x]
      prl[i][j][k] = sy
      print prl
      in_nd += 1		#numerará los nodos uno x uno hasta terminar cada celda de la matriz
      
