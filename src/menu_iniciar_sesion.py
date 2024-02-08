from empleados import EmpleadosDB

class MenuIniciarSesion:
    def __init__(self):
        self.empleados = EmpleadosDB()

    def load_database(self):
        self.empleados.load_database()
        
    def save_database(self):
        self.empleados.save_database() 

    def peticion_verificar_usuario(self, empleado_id, pin):
        verificado = self.empleados.verificar_empleado(empleado_id, pin)
        return verificado