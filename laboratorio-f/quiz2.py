print("OFERTAS El Emperador")

ofer1 = 0.30 
ofer2 = 0.20
ofer3 = 0.10


while clientes <5:
	monto = int(input("Ingrese monto: "))
	clientes += 1	
	if monto >= 500:
		subtotal =  monto * ofer1
		total = monto - subtotal
		print("El total es {0}: ".format(total)
		if monto < 500 or monto > 200
			subtotal = monto * ofer2
			total = monto + subtotal
			print("El total es {0}: ".format(total)
		if monto < 200: or monto > 100:
			subtotal = monto * ofer3
			total = monto + subtotal
			print("El total es {0}: ".format(total)
		else
			print("No hay descuento")
		
			print("gracias por su compra")
				break
