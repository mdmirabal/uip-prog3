n = 0
Tn = 0
print("NUMEROS TRIANGULARES")
nume = int (input("Ingrese el numero triangular: ""\n"))
for x in range (nume):
	tri = (x*(x+1))/2
	if int(tri) <= nume:
		print(str(tri))
	