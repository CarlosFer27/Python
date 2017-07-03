import Operaciones as op

print("Hola Fer\nSelecciona una de las siguientes opciones:\n")
print("1)Suma \n2)Resta \n3)Multiplicacion \n4)Division \n")
opcion = int(input())

if(opcion == 1):
	op.suma()
elif (opcion == 2):
	op.resta()
elif(opcion == 3):
	op.multiplicacion()
elif (opcion == 4):
	op.division()
else:
	print("Ingresaste una opcion incorrecta")
