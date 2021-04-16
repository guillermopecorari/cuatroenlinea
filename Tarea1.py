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
	for fila in tablero:
		print( )
		for columna in fila: 
			print(columna, end = ' ')

def columnavalida(secuencia):
	x=0
	for x in secuencia:
		if x > 7 or x < 1:
			return False
	return True


secuencia = [9,1,5,4,1,3,4,5]
if columnavalida(secuencia) == False:
	print("La secuencia no es valida")
else:
	dibujarTablero(completarTableroEnOrden(secuencia,tableroVacio())) 