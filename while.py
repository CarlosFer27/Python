# funcion input es para pedir datos de entrada

respuesta = "si"
numero = 0

while (respuesta == 'si'):
	numero = int(input("Ingresa un numero: "))
	if (numero > 0):
		print("El numero ingresado es positivo")
	elif (numero < 0):
		print("El numero ingresado es negativo")
	else:
		print("El numero ingresado es cero")
		
	respuesta = input("¿Quieres ingresar otro numero? si/no \n")
	if (respuesta == 'no'):
		print("Hasta Luego")
		
