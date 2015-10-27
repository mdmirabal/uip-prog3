op = 0
segundos = 0
while op < 6:
	tseg = int(input("Ingrese el tiempo en segundos""\n"))
	op += 1
	if tseg / 60:
		segundos = (60 - tseg) % 60
		print("\n"+str(segundos))