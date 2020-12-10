import json
with open ("tableros.json","r") as read_file:
	data = json.load(read_file)
	mov = data['movimientos']
	tbf = data['tbf']
	tba = data['tba']
	table= data['tablero']

def cab(matri,fin,o):
	F=[[0,0,0],[0,0,0],[0,0,0]]
	i = 0
	while(i < 3):
		j = 0
		while(j < 3):
			if (matri[i][j] != 0):
				paso = matri[i][j]
				matri[i][j] = 0
				unir(i,j,paso,F,o)
			j +=1
		i +=1
	for e in F:
		print (e)
	print ("")
	if (F != tbf):
		return cab(F,fin,o)

def unir(ti,tj,paso,ta,p):
	ob = table[ti][tj]
	for e in mov:
		if (ob == e[0]):
			i = 0
			while(i <= 2):
				j = 0
				while(j <= 2):
					if (table[i][j] == e[p]):
						ta[i][j] = paso
						return ta
					j += 1
				i += 1

print("Resultado \n")
cab(tba,tbf,1)