# -*- coding: utf-8 -*-
"""
Created on Sun Oct  4 14:30:14 2020

@author: juanc
"""
import json
Conocimiento = False

with open("base.json", "r") as read_file:
    data = json.load(read_file)
    Conocimiento = data['conocimiento']

def animales(A, B,C, CON):
    r = 0
    l = len(CON)
    while r != l:
        if CON[r][0] == A:
            if CON[r][1] == B:
                if CON[r][2] == C:
                    return True
        r += 1
    else:
        return False
    
def animales_red(A,B,C):
    return animales(A,B,C,Conocimiento)

def main():
    print("Bienvenido a este programa")
    print('Puedes escribir animales_red("<ANIMAL/CLASIFICACION>","<ES/TIENE/VIVE>","<G MAMARIAS/PROTECCION QUERATINA/SAUROPSIDOS/MAMMALIA/etc>")')
    print("Para salir escribe q o escribiendo quit()")
    Terminar = False
    while not Terminar:
        Leer = input("> ")
        if Leer == 'q':
            return
        Imprimir = eval(Leer)
        print(Imprimir)

if __name__ == '__main__':
    main()