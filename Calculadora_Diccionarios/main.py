import Operaciones as op
import pedir_datos as pd

ciclo_opciones = 1
opciones = {1:op.suma,2:op.resta,3:op.multiplicacion,4:op.division}

while(ciclo_opciones == 1):
	print("Selecciona una de las siguientes opciones\n")
	print("1)Suma \n2)Resta \n3)Multiplicacion \n4)Division")
	seleccion = int(input())
	if( seleccion < 1 or seleccion > 4 ):
		print("\nSeleccionaste una opcion incorrecta")
		sel_incorrect = 0
		while (sel_incorrect == 0):
			equivoque = int(input("\nQuieres volver a intentarlo?\n1)Si\n2)No\n"))
			if (equivoque == 1):
				sel_incorrect = equivoque
			elif(equivoque == 2):
				print("\nHasta luego")
				sel_incorrect = equivoque
				ciclo_opciones = equivoque
			else:
				print("\nSelecciona opcion correcta")
	else:
		num1 = pd.pedir_datos()
		num2 = pd.pedir_datos()
		resultado = opciones[seleccion](num1,num2)
		print("El resultado es: ",resultado)
		ot_oper = 0
		while (ot_oper == 0):
			otra_operacion = int(input("\nQuieres realizar otra operacion? \n1)Si\n2)No\n"))
			if (otra_operacion == 1):
				ciclo_opciones = otra_operacion
				ot_oper = 2
			elif(otra_operacion == 2):
				print("\nHasta luego")
				ot_oper = otra_operacion
				ciclo_opciones = otra_operacion
			else:
				print("Seleccionaste opcion incorrecta")
			
		
		



	

