def pedir_datos():
	""" Funcion dedicada a pedir un numero entero """
	num = int(input("Ingresa un numero: \n"))
	return num
	
def suma():
	"""Funcion que suma 2 numeros enteros"""
	num1 = pedir_datos()
	num2 = pedir_datos()
	suma = num1 + num2
	print ("La suma de",num1,"+",num2,"es igual a",suma)
	
def resta():
	"""Funcion que resta 2 numeros enteros"""
	num1 = pedir_datos()
	num2 = pedir_datos()
	resta = num1 - num2
	print ("La resta de",num1,"-",num2,"es igual a",resta)

def multiplicacion():
	"""Funcion que multiplica 2 numeros enteros"""
	num1 = pedir_datos()
	num2 = pedir_datos()
	multiplicacion = num1 * num2
	print("La multiplicacion de",num1,"*",num2,"es igual a",multiplicacion)

def division():
	"""Funcion que divide 2 numeros enteros"""
	num1 = pedir_datos()
	num2 = pedir_datos()
	division = num1 / num2
	print("La division de",num1,"/",num2,"es igual a",division)

