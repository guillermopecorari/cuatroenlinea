from src.Tarea1 import contenidoColumnas

def test_contenido_columnas():
	tablero = [
				[0,0,0,0,0,0,0],
				[0,0,0,0,0,1,0],
				[2,0,0,0,0,1,1],
				[1,0,0,0,0,1,2],
				[2,0,1,1,0,2,2],
				[1,1,2,2,2,1,2],
			]
	assert contenidoColumnas(tablero) == [
										[0,0,2,1,2,1],
										[0,0,0,0,0,1],
										[0,0,0,0,1,2],
										[0,0,0,0,1,2],
										[0,0,0,0,0,2],
										[0,1,1,1,2,1],
										[0,0,1,2,2,2]
										]