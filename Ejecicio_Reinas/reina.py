import copy

def get_tablero(tamaño):
    tablero = [0] * tamaño
    for x in range(tamaño):
        tablero[x] = [0] * tamaño
    return tablero


def impri_solu(solucion, reina):
    for sol in solucion:
        for fila in sol:
            print(fila)
        print()


def proce(tablero, fila, col, tamaño):
    for y in range(col):
        if tablero[fila][y] == 1:
            return False
    x, y = fila, col
    while x >= 0 and y >= 0:
        if tablero[x][y] == 1:
            return False
        x -= 1
        y -= 1
    x, y = fila, col
    while x < tamaño and y >= 0:
        if tablero[x][y] == 1:
            return False
        x += 1
        y -= 1
    return True


def resolver(tablero, col, tamaño):
    if col >= tamaño:
        return
    for i in range(tamaño):
        if proce(tablero, i, col, tamaño):
            tablero[i][col] = 1
            if col == tamaño - 1:
                añadir_tab(tablero)
                tablero[i][col] = 0
                return
            resolver(tablero, col + 1, tamaño)
            tablero[i][col] = 0


def añadir_tab(tablero):
    global soluc
    guardar_tab = copy.deepcopy(tablero)
    soluc.append(guardar_tab)


reina = 4
tablero = get_tablero(reina)
soluc = []
resolver(tablero, 0, reina)
impri_solu(soluc, reina)

print("Soluciones = {}".format(len(soluc)))