#!/usr/bin/python
# -*- coding: utf-8 -*-

from sympy import *


#DEclaracion de variables
h = 0.999999999999	#condicion de temperaturas
R = 12	#temperatura refrigerante
A = 0	#condicion Cara Aislante
B = 60	#condicion 4

dx = 0.25
dy = 0.1
dz = 0.5

xx=4
#xy=4
z=5

#xx= int(round(xx/dx))		#dx dy dz son variaciones dif_finitias del nodo para calcular dimensiones correctas de la matriz 3D
#xy = int(round(xy/dy))		#las deja en entero para poder generar la matriz 3D
#z= int(round(z/dz))

#<********************Declaracion de métodos

def mostrar(texto):
  print "************************{}******************************".format(texto)

  for i in range(0,z):		#relleno con las variables "symbolic" a nodos equisdistantes
    print "Cara {}".format(i)
    for j in range(0,xx):		#por dentro de la superficie
      for k in range(0,xx):
	if prl[i][j][k] != "":
	  print prl[i][j][k],
	else:
	  print "\t",
	#print "{} \t".format(prl[i][j][k])
      print "\n"

def ddty(x,y,z,j):		#Condiciones de newman
  if j==1:
    z = x-2*dy*h*(x-R)
  elif j== xx-2:
    x = z-2*dy*h*(z-R)
  yyy = (x-2*y+z)/(dy*dy)
  return yyy

def ddtx(x,y,z,i):
  if i==1:
    z = x-2*dy*h*(x-R)
  elif i==xx-2:
    x = z-2*dy*h*(z-R)
  xxx = (x-2*y+z)/(dx*dx)
  return xxx

def ddtz(x,y,z,k):
  if k==1:
    z = x-2*dy*h*(x-R)
  elif k==z-2:
    x = z-2*dy*h*(z-R)
  zzz = (x-2*y+z)/(dz*dz)
  return zzz



#Inicio del programa principal

prl = [[["" for x in xrange(xx)] for x in xrange(xx)] for x in xrange(z)]

for i in range(0,z):		#rellenado condiciones de borde
    for j in range(0,xx):
      prl[i][0][j] = R
      prl[i][xx-1][j] = R
      prl[i][j][0] = R
      prl[i][j][xx-1] = R

mostrar("Condiciones de Borde")
      
  
for i in range(1,xx-1):		#Rellenando condiciones en caras
  for j in range(1,xx-1):
    prl[0][i][j] = A
    prl[z-1][i][j] = B

mostrar("Condiciones en Caras")

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

mostrar("LLenado")    

#x = ["" for x in range(xx*z)] generar vector para generar matriz H[x*y*z] y rellenar con ecuación elíptica de nodos
#despues generar matriz con datos de tipo A[x*y*z,x*y*z] y vector B[x*y*z] a incógnitas de tipo Ax=B
w = ["" for x in range((xx-1)*(z-1)*(xx-1))] 

#Recorriendo matriz
in_nd = 0
for i in range(1,z-1):		#relleno con las variables "symbolic" a nodos equisdistantes
  print "Cara {}".format(i)
  for j in range(1,xx-1):		#por dentro de la superficie
    for k in range(1,xx-1):
      w[in_nd] = ddtx(prl[i][j][k+1],prl[i][j][k],prl[i][j][k-1],k) + ddty(prl[i][j+1][k],prl[i][j][k],prl[i][j-1][k-1],j) + ddtx(prl[i+1][j][k],prl[i][j][k],prl[i-1][j][k],i)
      in_nd += 1		#numerará los nodos uno x uno hasta terminar cada celda de la matriz	

for i in range(len(w)):
  print w[i]
