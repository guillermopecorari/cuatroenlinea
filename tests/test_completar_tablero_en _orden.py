from src.Tarea1 import completarTableroEnOrden

def test_completar_tablero_en_orden():
	tablero = [
				[0,0,0,0,0,0,0],
				[0,0,0,0,0,0,0],
				[0,0,0,0,0,0,0],
				[0,0,0,0,0,0,0],
				[0,0,0,0,0,0,0],
				[0,0,0,0,0,0,0],
			]

	secuencia = [1,2,3,4,5,6,7]
	completarTableroEnOrden(secuencia,tablero)

	assert tablero[5] == [1,2,1,2,1,2,1]