from pickle import load, dump
from joya import Joya

class SubsistemaAlmacenamiento:
    def __init__(self):
        self.inventario = []
        
    def save_inventario(self):
        try:
            with open('inventario', "wb") as file:
                dump(self.inventario, file)
        except Exception as e:
            print("...Ocurrio un error al guardar el inventario: ", e, "\n")
        else:
            print("...Inventario guardado con exito\n")
    
    def load_inventario(self):
        try:
            with open('inventario', "rb") as file:
                self.inventario = load(file)
        except Exception as e:
            print("...Ocurrio un error al cargar el inventario: ", e, "\n")
        else:
            print("...Inventario cargado con exito\n")
        
    def agregar_inventario(self, joya):
        self.inventario.append(joya)
        self.save_inventario()   

    def alta(self, modelo, nombre, marca, material, color, tipo, tipoPiedra, precio):
        joya = Joya(modelo, nombre, marca, material, color, tipo, tipoPiedra, precio)
        self.agregar_inventario(joya)
        return joya
        
    def baja(self, modelo_nombre):
        for joya in self.inventario:
            if joya.getModelo() == modelo_nombre or joya.getNombre() == modelo_nombre:
                self.inventario.remove(joya)
                self.save_inventario()
                return True
        return False
    
    def consulta(self, modelo_nombre):
        for joya in self.inventario:
            if joya.getModelo() == modelo_nombre or joya.getNombre() == modelo_nombre:
                print("...Joya encontrada\n")
                return joya
        print("...Joya no encontrada\n")
        return None

    def modificacion(self, tipo_modificacion, nuevo_valor, joya):
        if tipo_modificacion == 1:
            joya.setNombre(nuevo_valor)
        else:
            joya.setPrecio(nuevo_valor)
        self.save_inventario()
        return joya
