def tableroVacio():
	return	[
				[0,0,0,0,0,0,0],
				[0,0,0,0,0,0,0],
				[0,0,0,0,0,0,0],
				[0,0,0,0,0,0,0],
				[0,0,0,0,0,0,0],
				[0,0,0,0,0,0,0],
			]

def soltarFichaEnColumna(ficha,columna,tablero):
    for fila in range(6,0,-1):
        if tablero[fila - 1][columna - 1] == 0:
            tablero[fila - 1][columna - 1] = ficha
            return

def completarTableroEnOrden(secuencia,tablero):
	x = 0
	for i in secuencia:
		if x % 2 == 0:
			soltarFichaEnColumna(1, i, tablero)
		else:
			soltarFichaEnColumna(2, i, tablero)
		x = x + 1
	return tablero

def dibujarTablero(tablero):
	print()
	for fila in tablero:
		print("|",end = ' ')
		for columna in fila: 
			print(str(columna).replace('0',' '), end = '  ')
		print("|")
	print("+----------------------+")

def columnavalida(secuencia):	
	for x in secuencia:
		if x > 7 or x < 1:
			return False
	return True

def contenidoColumna(nro_columna, tablero):
	columna = []
	for fila in tablero:
		celda = fila[nro_columna - 1]
		columna.append(celda)
	return columna

def contenidoFila(nro_fila, tablero):
	fila = []
	x = 0
	for columna in tablero:
		x += 1
		if x == nro_fila:
			for celda in columna:
				fila.append(celda)
	return fila

def contenidoFilas(tablero):
	filas = []
	x = 1
	for columna in tablero:
		filas.append(contenidoFila(x,tablero))
		x += 1
	return filas

def contenidoColumnas(tablero):
	columnas = []
	x = 1
	for fila in tablero:
		columnas.append(contenidoColumna(x,tablero))  
		x += 1                               
	return columnas

tablero = []
secuencia = [1,2,4,6,2,3,1]
if columnavalida(secuencia) == False:
	print("La secuencia no es valida")
else:
	tablero = completarTableroEnOrden(secuencia,tableroVacio())
	dibujarTablero(tablero)

#print(contenidoColumnas(tablero))