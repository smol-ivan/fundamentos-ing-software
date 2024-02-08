class TicketDeVenta:
    def __init__(self, precio, formaDePago, articulos, fecha, sucursal):
        self.precio = precio
        self.formaDePago = formaDePago
        self.articulos = articulos
        self.fecha = fecha
        self.sucursal = sucursal

    def imprimirTicket(self):
        # Implementar lógica de impresión de ticket
        pass

    def getArticulos(self):
        # Obtener la lista de artículos en el ticket
        return self.articulos