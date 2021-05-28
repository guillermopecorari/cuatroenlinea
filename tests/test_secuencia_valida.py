from src.Tarea1 import secuenciaValida

def test_secuencia_valida():
	secuencia = [1,2,4,5]

	assert secuenciaValida(secuencia) == True