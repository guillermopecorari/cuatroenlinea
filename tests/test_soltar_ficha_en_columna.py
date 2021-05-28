from src.Tarea1 import soltarFichaEnColumna

def test_soltar_ficha_en_columna():
	tablero = [
				[0,0,0,0,0,0,0],
				[0,0,0,0,0,0,0],
				[0,0,0,0,0,0,0],
				[0,0,0,0,0,0,0],
				[0,0,0,0,0,0,0],
				[0,0,0,0,0,0,0],
			]
	soltarFichaEnColumna(1,6,tablero)
	
	assert tablero[5][5] == 1