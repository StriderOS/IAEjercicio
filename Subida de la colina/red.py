import json
import random
from operator import itemgetter

with open('conocimiento.json') as file:
    Conocimiento = json.load(file)

camin = []
nodos = []
camP = []


def buscar(inicio, fin):
    fi = 0
    anterior = ""
    iteracion = 1
    while (fi == 0):
        nodos = [n for n in Conocimiento if (n[0] == inicio and n[1] != anterior)]
        valMen = (min(nodos, key=itemgetter(2))[2])

        cp = [cp for cp in nodos if (cp[2] == valMen and cp[1] != anterior)]

        if (len(cp) > 1):
            seguir = 0
            indice = random.randint(0, len(camP) - 1)
            cuentaPasos = 1
            while (seguir == 0):
                menor = cp[indice]
                if (len([item for item in camin if item[1] == menor[1]]) == 0 and len([item for item in camin if item[0] == menor[1]]) == 0):
                    seguir = 1
                cuentaPasos += 1
                if (cuentaPasos > len(cp)):
                    seguir = 1
                    fi = 1
                    print(' No se ha podido llegar ')
        else:
            menor = cp[0]
        camin.append(menor)
        siguiente = menor[1]
        anterior = inicio
        if (siguiente == fin):
            fi = 1
        else:
            inicio = siguiente
        iteracion += 1

print("La ruta es: \n")
buscar("A", "G")
print(camin)