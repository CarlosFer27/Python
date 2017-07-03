contador = 1
while(contador == 1):
	contrasena = input("\nIngresa tu contraseña: \n")
	blancos = contrasena.find(" ")
	if(len(contrasena) < 8 or contrasena.isalnum() == True or contrasena.isupper() == True or contrasena.islower() == True or blancos != -1):
		print("\nLa contraseña elegida no es segura")
	else:
		print("True")
		contador = 2
		
	
