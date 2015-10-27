class Hola(object):
  __contador = 0

  def __init__(self):
    pass
  def ingresar_mensaje(self):
    self.mensaje = input("Ingrese el Mensaje que Desea: ").title()

  def comparar_mensaje(self):
    if self.mensaje == ("Hola Mundo"):
      print("Es igual")
    else:
      print("no es igual")  
  
  def mostrar_contador(self):
    self.__contador += 1
    print(str( self.__contador))

  def guardar_mensaje(self):
    archivo = open("men.txt", "w")
    archivo.close()

    archivo = open("men.txt", "a")
    archivo.write("El Mensaje Fue: "+self.mensaje)
    archivo.write("\n Contador: "+str(self.__contador))

    archivo.close()


