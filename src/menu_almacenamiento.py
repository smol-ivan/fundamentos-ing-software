from menu import Menu
from sys_almacenamiento import SubsistemaAlmacenamiento

class MenuAlmacenamiento(Menu):
    def __init__(self):
        self.sys_almacenamiento = SubsistemaAlmacenamiento()

    def datos_joya(self):
        print("Por favor ingrese los datos de la joya")
        modelo = input("Modelo: ")
        nombre = input("Nombre: ")
        marca = input("Marca: ")
        material = input("Material: ")
        color = input("Color: ")
        tipo = input("Tipo: ")
        tipoPiedra = input("Tipo de piedra: ")
        precio = input("Precio: ")
        return modelo, nombre, marca, material, color, tipo, tipoPiedra, precio
    
    def imprimir_joya(self, joya):
        print(joya.__str__())
    
    def peticion_alta(self):
        modelo, nombre, marca, material, color, tipo, tipoPiedra, precio = self.datos_joya()
        joya = self.sys_almacenamiento.alta(modelo, nombre, marca, material, color, tipo, tipoPiedra, precio)
        self.imprimir_joya(joya)

    def peticion_consulta(self):
        modelo_nombre = input("Ingrese el modelo o nombre de la joya: ")
        joya = self.sys_almacenamiento.consulta(modelo_nombre)
        if joya is not None:
            self.imprimir_joya(joya)
        else:
            print("...Joya no encontrada\n")

    def peticion_baja(self):
        modelo_nombre = input("Ingrese el modelo o nombre de la joya: ")
        if self.sys_almacenamiento.baja(modelo_nombre):
            print("...Joya eliminada\n")
        else:
            print("...Joya no encontrada\n")

    def peticion_modificacion(self):
        modelo_nombre = input("Ingrese el modelo o nombre de la joya: ")
        joya = self.sys_almacenamiento.consulta(modelo_nombre)
        if joya:
            #Mostrar opciones de modificacion
            print("~Seleccione el campo a modificar")
            print("1.Nombre")
            print("2.Precio")
            opcion = self.seleccion_opcion(2)
            if opcion == 1:
                nombre = input("Ingrese el nuevo nombre: ")
                nueva_joya = self.sys_almacenamiento.modificacion(1, nombre, joya)
            else:
                precio = input("Ingrese el nuevo precio: ")
                nueva_joya = self.sys_almacenamiento.modificacion(2, precio, joya)
            print("...Joya modificada con exito")
            self.imprimir_joya(nueva_joya)
        

    def mostrar_menu(self):
        self.sys_almacenamiento.load_inventario()
        regresar = False
        while not regresar:
            print("1.Añadir joya")
            print("2.Consultar joya")
            print("3.Modificar informacion joya")
            print("4.Baja de joya")
            print("5.Regresar\n")
            
            opcion = self.seleccion_opcion(5)
            if opcion == 1:
                self.peticion_alta()
            elif opcion == 2:
                self.peticion_consulta()
            elif opcion == 3:
                self.peticion_modificacion()
            elif opcion == 4:
                self.peticion_baja()
            else:
                regresar = True
                self.sys_almacenamiento.save_inventario()
            
