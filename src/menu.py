class Menu:
    def __init__(self) -> None:
        pass
        
    def seleccion_opcion(self, num_opciones):
        opcion_valida = False
        while not opcion_valida:
            seleccion = input('~Seleccione una opcion (num): ')
            if seleccion.isdigit() and int(seleccion) >= 0 and int(seleccion) <= num_opciones:
                opcion_valida = True
            else:
                print('Opcion invalida, intente de nuevo')
        opcion_escogida = int(seleccion)
        return opcion_escogida