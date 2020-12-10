import json
import random
from operator import itemgetter

with open('conocimiento.json') as file:
    Conocimiento = json.load(file)

r = []
nodos = []
camP = []


def ruta(inicio, fin):
    fina = 0
    anterior = ""
    iteracion = 1
    while (fina == 0):
        nodos = [n for n in Conocimiento if (n[0] == inicio and n[1] != anterior)]
        valMen = (min(nodos, key=itemgetter(2))[2])

        camP = [cp for cp in nodos if (cp[2] == valMen and cp[1] != anterior)]

        if (len(camP) > 1):
            seguir = 0
            indice = random.randint(0, len(camP) - 1)
            cuentaPasos = 1
            while (seguir == 0):
                menor = camP[indice]
                #
                if (len([item for item in r if item[1] == menor[1]]) == 0 and len([item for item in r if item[0] == menor[1]]) == 0):
                    seguir = 1
                cuentaPasos += 1
                if (cuentaPasos > len(camP)):
                    seguir = 1
                    fina = 1
                    print(' No se ha podido llegar al objetivo; nueva ruta  ')
        else:
            menor = camP[0]
        r.append(menor)
        siguiente = menor[1]
        anterior = inicio

        if (siguiente == fin):
            fina = 1
        else:
            inicio = siguiente
        iteracion += 1

print("Ruta \n")
ruta("A", "L")
print(r)