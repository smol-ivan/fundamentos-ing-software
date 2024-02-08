from sys_venta import SubsistemaDeVenta
from menu import Menu

class MenuVenta(Menu):
    def __init__(self):
        self.sys_venta = SubsistemaDeVenta()

    def mostrar_menu(self):
        regresar = False
        while not regresar:
            print("Proximamente...")
            print("1. Regresar")
            opcion = self.seleccion_opcion(1)
            if opcion == 1:
                regresar = True