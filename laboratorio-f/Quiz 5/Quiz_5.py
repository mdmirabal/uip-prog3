from main import Hola
from menu import menu

class HolaMundo(Hola):
    def menu(self):
      opc = 0
      opciones =("Ingresar mensaje","Comparar mensaje","Guardar mensaje",
                  "Mostrar contador","Salir")
      while opc <5: 
        opc = menu("principal",*opciones)
        if opc == 1:
          objeto.ingresar_mensaje()
        elif opc == 2:
          objeto.comparar_mensaje()
        elif opc == 3:
          objeto.guardar_mensaje()
        elif opc == 4:
          objeto.mostrar_contador()
        elif opc == 5:
          print()
        #input("Presione una tecla para continuar...")
      else:
        print("\nFin\n".center(90, "#"))

if __name__ == '__main__':
  objeto= HolaMundo()
  objeto.menu()
print("Hasta luego!")