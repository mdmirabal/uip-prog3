op = 0
horas = 0
dias = 0
while op <6:
	minutos = int(input("Ingrese el tiempo en minutos""\n"))
	op += 1
	if minutos / 60:
		horas = minutos / 60 
		dias = minutos / 1440
		print(str(dias) +" Dias")
		print(str(horas) +" Horas")
		print(str(minutos) +" Minutos")
		break