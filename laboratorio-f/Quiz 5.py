class Hola(object):
	__contador = 0

def __init__(self):

	def mostrar_contador(self):
		self.__contador += 1
		print(str(__contador))

	def comparar_mensaje(self, msj):
		self.mensaje = msj
		if msj == "Hola Mundo"
			print("Es igual")
		else:
			print("no es igual")

	def guardar_mensaje(self):

class HolaMundo(Hola):

	def Menu():
		print('1. Ingresar mensaje')
		print('2. Comparar mensaje')
		print('3. Guardar mensaje')
		print('4. Mostrar contador')
		print('5. Salir')
		print()

if __name__ == '__main__':
  	opcion_menu = 0
  	while True:
  		Menu1()
  		try:
  			opcion_menu = int(input("Indica una opcion (1-5): "))
  		except:
  			print("Opcion no valida")
  		else:
  			if opcion_menu == 1:
  				mensaje = intput("Ingrese un mensaje: ")
  			elif opcion_menu == 2:
  				print("Comparar mensaje")
  				comparar_mensaje(msj)
  			elif opcion_menu == 3:
  				print("guardar mensaje")
  				guardar_mensaje()
  			elif opcion_menu == 4:
  				print("mostrar contador")
  				mostrar_contador(__contador)
  			elif opcion_menu == 5:
  				break
  			else:
  				print("Opcion no valida")
  				Menu1()
  	print("Hasta luego!")
