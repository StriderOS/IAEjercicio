# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 23:48:40 2020

@author: juanc

PROFUNDIDAD

"""
import json
JSONDATA = False
with open('base.json','r') as f:
	JSONDATA = json.load(f)

raiz = input("Ingrese el valor de la raiz: ")
eab = input("Ingrese el valor a buscar: ")
ruta=[]
 
def buscar(inicio,valorBuscar):
    ruta.append(inicio)
    if inicio==valorBuscar:
        return valorBuscar
    for i,j in JSONDATA['Base'].items():
        if j==inicio:
            result=buscar(i,valorBuscar)
            if result:
                return result 
    ruta.pop()
    return 0

result=buscar(raiz,eab)
if result:
    print(ruta)
else:
    print("Ruta NO encontrada")