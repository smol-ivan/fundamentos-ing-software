from sys_citas import SubsistemaDeCitas
from menu import Menu

class MenuCitas(Menu):
    def __init__(self):
        self.sys_citas = SubsistemaDeCitas()
        
    def mostrar_menu(self):
        regresar = False
        while not regresar:
            print("Proximamente...")
            print("1. Regresar")
            opcion = self.seleccion_opcion(1)
            if opcion == 1:
                regresar = True
         