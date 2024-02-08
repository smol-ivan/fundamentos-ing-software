from pickle import load, dump

class EmpleadosDB:
    def __init__(self):
        self.database = {'empleado1': 1235}

    def load_database(self):
        try:
            with open('database_empleados', "rb") as file:
                self.database = load(file)
        except FileNotFoundError:
            print('...Base de datos de Empleados no encontrada, verifique los archivos del sistema')
        else:
            print('...Base de datos de empleados cargada')
    
    def save_database(self):
        try:
            with open('database_empleados', "wb") as file:
                dump(self.database, file)
        except Exception as e:
            print(f'...Error al guardar la base de datos de empleados: {e}')
        else:
            print('...Base de datos de empleados guardada')
            
    def verificar_empleado(self, empleado_id, pin):
        verificado = False

        if empleado_id not in self.database: 
            print("ID no encontrado\n")
            return verificado

        if pin != self.database[empleado_id]:
            print("PIN no incorrecto\n")
            return verificado
        
        verificado = True

        return verificado
        
            