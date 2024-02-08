class Cita:
    def __init__(self, tipoMantenimiento, fecha, sucursal, tipoJoya, modelo):
        self.tipoMantenimiento = tipoMantenimiento
        self.fecha = fecha
        self.sucursal = sucursal
        self.tipoJoya = tipoJoya
        self.modelo = modelo

    def getFecha(self):
        # Obtener la fecha de la cita
        return self.fecha

    def getTipoMantenimiento(self):
        # Obtener el tipo de mantenimiento de la cita
        return self.tipoMantenimiento

    def getSucursal(self):
        # Obtener la sucursal de la cita
        return self.sucursal

    def getTipoJoya(self):
        # Obtener el tipo de joya de la cita
        return self.tipoJoya

    def getModelos(self):
        # Obtener la lista de modelos en la cita
        return self.modelo

    def setTipoMantenimiento(self, tipoMantenimiento):
        # Establecer el tipo de mantenimiento de la cita
        self.tipoMantenimiento = tipoMantenimiento

    def setSucursal(self, sucursal):
        # Establecer la sucursal de la cita
        self.sucursal = sucursal

    def setTipoJoya(self, tipoJoya):
        # Establecer el tipo de joya de la cita
        self.tipoJoya = tipoJoya

    def setModelos(self, modelo):
        # Establecer la lista de modelos en la cita
        self.modelo = modelo