def fibonacci():
    anterior = 0
    siguiente = 1
    limite = int(input("Ingresa el numero limite: "))
    while(anterior < limite) :
    	print(anterior)
    	guardar = anterior
    	anterior = siguiente
    	siguiente = guardar + siguiente
