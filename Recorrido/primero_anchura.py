# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 23:50:29 2020

@author: juanc
ANCHURA
"""
import json
JSONDATA = None
with open('base.json','r') as f:
	JSONDATA = json.load(f)
	
raiz = input("Ingrese el valor de la raiz: ")
eab = input("Ingrese el valor a buscar: ")

camino=[]
 
fifo=[]
 
def buscar(inicio,valorBuscar,iteraciones):

    camino.append(inicio)
 
    if inicio==valorBuscar:
        return (True,iteraciones)
 
    fifoAdd(inicio)
 
    if len(fifo)==0:
        return (False,iteraciones)
 
    return buscar(fifo.pop(0),valorBuscar,iteraciones+1)
 
def fifoAdd(inicio):

    for k,v in JSONDATA['Base'].items():
        if v==inicio:
            fifo.append(k)
 
resultado,iteraciones=buscar(raiz,eab,1)
if resultado:
    print("Se ha encontrado el valor en {} iteraciones".format(iteraciones))
else:
    print("No se ha encontrado")
print("La ruta trazada fue: {}".format(camino))