from src.Tarea1 import contenidoFila

def test_contenido_fila():
	tablero = [
				[0,0,0,0,0,0,0],
				[0,0,0,0,0,1,0],
				[2,0,0,0,0,1,1],
				[1,0,0,0,0,1,2],
				[2,0,1,1,0,2,2],
				[1,1,2,2,2,1,2],
			]
	assert contenidoFila(6,tablero) == [1,1,2,2,2,1,2]