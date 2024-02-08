# Manual de uso

## Instrucciones de descarga

- La aplicacion funciona de manera local, lo cual es necesario clonar el repositorio, los pasos son los siguientes
1. Desde la terminal tenemos que estar en la carpeta donde queremos que se descargue el repositorio, por ejemplo
    ```console
    @smol-ivan ➜ /workspaces $ 
    ```
2. Solo queda hacer gir clone al respositorio
    ```console
    git clone https://github.com/smol-ivan/fundamentos-ing-software.git
    ```
    
## Instrucciones de Uso

1. Para la ejecucion de la aplicacion se hace desde el archivo que llama por nombre `main.py` que se encuentra alojado en la carpeta `/src` de este repositorio
    ```console
    py main.py
    ```
    > La llamada al programa con python puede variar dependiento el sistema `python`, `python3`
2. Una vez iniciada la aplicacion se pedira el inicio de sesion para acceder a las funcionalidades
    - <sub>Por motivos de practica el sistema ya considera a un solo empleado, que se identifica en el sistema como:</sub>
        - <sub>ID : `empleado1`</sub>
        - <sub>PIN: `1235`</sub>
3. Cuando se verifique el usuario, se da acceso a los submenus del sistema. Para navegar en la interfaz solo basta teclear la opcion deseada
4. Para el menu almacenamiento las operaciones que requieran hacer cambios(alta, baja, modificar) una vez realizada la operacion el sistema guarda actualiza automaticamente la base de datos

### Para las operaciones de consulta, modificacion y baja
- Estas operaciones realizan primero la busqueda de la joya en la base de datos, por lo que es necesario contar con el modelo o nombre de la joya deseada!

## Consideraciones

- El sistema esta cargado previamente con un inventario de joyas, las cuales se identifican como:

| Joya | ID  | Modelo |
| ---- |:-:|:----:|
|Anillo de Oro | 123 | Anillo de Oro |
|Pulsera de Plata | 245 | Pulsera de Plata |
