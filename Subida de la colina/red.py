
import json

Datos = False

with open('conocimiento.json','r') as info:
    data = json.load(info)
    Datos = data["Datos"]

def Camino(camino):
    vA = 0
    vM = 0
    L = []
    for i in camino:
        if vA == 0:
            L.append(i)
            vA = i[2]
        else:
            if i[2] <= vA:
                vM = i[2]
                vA = i[2]
                L = []
                L.append(i)
            else:
                vM = vA
                vA = i[2]
    return L


def subirColina():
    lR = []
    valor = str(input('Valor a llegar: '))
    Elemento = [ e for e in Datos if e[1] == valor]
    lR.append(Elemento[0])
    while Elemento[0][0] != Datos[0][0]:
        Elemento = [ e for e in Datos if e[1] == Elemento[0][0]]
        if len(Elemento) > 1:
            Elemento = Camino(Elemento)
            lR.append(Elemento[0])
        else:
            lR.append(Elemento[0])
    return lR

A = subirColina()
if type(A) == list:
    A = A[::-1]


print("Camino a seguir: ",A)