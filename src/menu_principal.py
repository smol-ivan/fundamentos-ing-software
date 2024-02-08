from menu_almacenamiento import MenuAlmacenamiento
from menu_citas import MenuCitas
from menu_iniciar_sesion import MenuIniciarSesion
from menu_venta import MenuVenta
from menu import Menu

class MenuPrincipal(Menu):
    def __init__(self):
        self.submenu_almacenamiento = MenuAlmacenamiento()
        self.submenu_citas = MenuCitas()
        self.submenu_iniciar_sesion = MenuIniciarSesion()
        self.submenu_ventas = MenuVenta()
        self.usuario_verificado = False

    def catch_pin(self):
        es_valido = False
        while not es_valido:
            seleccion = input('PIN: ')
            if seleccion.isdigit() and int(seleccion) >= 0 and int(seleccion) < 10000:
                es_valido = True
            else:
                print("PIN con formato invalido. Formato 'XXXX'\n")
        pin = int(seleccion)
        return pin
    
    def datos_iniciar_sesion(self):
        intentos = 3
        print("Por favor ingrese su id y pin\n")
        while not self.usuario_verificado and  intentos > 0:
            empleado_id = input("Ingrese su ID: ")
            pin = self.catch_pin()
            if self.submenu_iniciar_sesion.peticion_verificar_usuario(empleado_id, pin):
                self.usuario_verificado = True
                print("\tBienvenido al sistema!.\n")
            else:
                intentos -= 1
                if intentos == 0:
                    print("Ha excedido el numero de intentos permitidos, el sistema se cerrara\n")
                    exit()
                print(f"Intente de nuevo, intentos restantes {intentos}. \n")
        
                

    def principal(self):
        if not self.usuario_verificado:
            self.datos_iniciar_sesion()
            
        # Menu principal
        regresar = False
        while not regresar:
            print("1.Menu almacenamiento")
            print("2.Menu venta")
            print("3.Menu citas")
            print("4.Salir\n")

            opcion = self.seleccion_opcion(4)
            if opcion == 1:
                self.submenu_almacenamiento.mostrar_menu()
            elif opcion == 2:
                self.submenu_ventas.mostrar_menu()
            elif opcion == 3:
                self.submenu_citas.mostrar_menu()
            else:
                regresar = True
                print("...Saliendo del sistema\n")

    def iniciar_sistema(self):
        print("\tSISTEMA JOYERIA\n")
        self.submenu_iniciar_sesion.load_database()
        self.principal()