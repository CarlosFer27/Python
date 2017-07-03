#ejemplo For para tabla de multiplicar

mi_lista = [1,2,3,4,5,6,7,8,9,10]

tabla = int(input("Que tabla de multiplicar quieres mostrar? "))
for contador in mi_lista:
	resultado = tabla * contador
	print(tabla,"*",contador,"=",resultado)

