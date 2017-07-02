def pedir_dato():
	"""Funcion dedicada a pedir un numero"""
	numero = int(input("Ingresa un numero: \n"))
	return numero
	
def suma():
	"""Funcion que suma 2 numeros"""
	num1 = pedir_dato()
	num2 = pedir_dato()
	suma = num1 + num2
	print ("El resultado de",num1,"+",num2,"es igual a", suma)
	
def resta():
	"""Funcion que resta 2 numeros"""
	num1 = pedir_dato()
	num2 = pedir_dato()
	resta = num1 - num2 
	print ("El resultado de",num1," - ",num2," es igual a ",resta)
	
def multiplicacion():
	"""Funcion que multiplica 2 numeros"""
	num1 = pedir_dato()
	num2 = pedir_dato()
	multiplicacion = num1 * num2
	print ("El resultado de",num1,"*",num2,"es igual a",multiplicacion)

def division():
	"""Funcion que divide 2 numeros"""
	num1 = pedir_dato()
	num2 = pedir_dato()
	division = num1 / num2
	print ("El resultado de",num1,"/",num2,"es igual a",division)
	
