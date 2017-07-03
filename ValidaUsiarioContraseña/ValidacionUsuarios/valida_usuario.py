contador = 1
while(contador == 1):
	nombre = input("\nIngresa tu usuario: ")
	caracteres = len(nombre)
	alfanumerico = nombre.isalnum()
	
	if(caracteres < 6):
		print("\nEl nombre de usuario debe contener al menos 6 caracteres")
	elif(caracteres > 12):
		print("\nEl nombre de usuario no puede contener más de 12 caracteres")
	elif(alfanumerico == False):
		print("\nEl nombre de usuario puede contener solo letras y números")
	else:
		print(True)
		contador = 2
