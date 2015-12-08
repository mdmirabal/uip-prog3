from kivy.app import App

lista = []

def guardar(name):
	lista.append(name)
	print(lista)	
	
def exportar():
	archivo = open('asistencia.txt', 'wt')
	archivo.write(str(lista))
	archivo.close()

class AsistenciaApp(App):
	
	def build (self):
		pass
	
	
	
if __name__ == '__main__':
	AsistenciaApp().run()
