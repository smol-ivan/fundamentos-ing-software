class Joya:
    def __init__(self, modelo, nombre, marca, material, color, tipo, tipoPiedra, precio):
        self.modelo = modelo
        self.nombre = nombre
        self.marca = marca
        self.material = material
        self.color = color
        self.tipo = tipo
        self.tipoPiedra = tipoPiedra
        self.precio = precio
        
    def __str__(self):
        return f"~Modelo: {self.modelo}\n~Nombre: {self.nombre}\n~Marca: {self.marca}\n~Material: {self.material}\n~Color: {self.color}\n~Tipo: {self.tipo}\n~Tipo de piedra: {self.tipoPiedra}\n~Precio: {self.precio}\n"

    def getModelo(self):
        return self.modelo

    def getNombre(self):
        return self.nombre

    def setNombre(self, nombre):
        self.nombre = nombre

    def setPrecio(self, precio):
        self.precio = precio