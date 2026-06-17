def mostrarMenu():

    print("===== MENÚ PRINCIPAL =====")
    print("1. Agregar vehiculo")
    print("2. Buscar vehiculo")
    print("3. Eliminar vehiculo")
    print("4. Actualizar disponibilidad")
    print("5. Mostrar vehiculos")
    print("6. Salir")
    print("==========================")

def opcion_menu():

    while True:
        try:
            opcionMenu = int(input("Ingrese una opcion del menu: "))

            if opcionMenu >= 1 and opcionMenu <= 6:
                return opcionMenu
            else:
                print("Error: Debe ingresar una opcion válida! (1-6)")
        except ValueError:
            print("ERROR: Debe ingresar una opcion válida!")

def agregar_vehiculo(listadoVehiculo):

    modelo = input("Ingrese modelo del vehiculo: ")
    año = input("Ingrese año del vehiculo: ")
    precio = input("Ingrese precio del vehiculo: ")

    modeloValido = validar_modelo(modelo)
    añoValido = validar_año(año)
    precioValido = validar_precio(precio)

    if modeloValido and añoValido and precioValido:

        vehiculo = {
            "modelo" : modelo,
            "año" : int(año),
            "precio" : float(precio),
            "disponible" : False
        }
        listadoVehiculo.append(vehiculo)
        print("Vehículo agregado éxitosamente!")
    else:
        print("ERROR: Los datos no cumplen con los valores correctos.")
   

def validar_modelo(modelo):

    if modelo.strip() == "":
        return False
    else:
        return True
    
def validar_año(año):

    try:
        añoNum = int(año)

        if añoNum < 1900:
            return False
        else:
            return True
    except ValueError:
        return  False
    
def validar_precio(precio):

    try:
        precioDeci = float(precio)
        
        if precioDeci > 0:
            return True
        else:
            return False
    except ValueError:
        return False
    
def buscarVehiculo(lista, modelo):

    for indice, vehiculo in enumerate(lista):
        if modelo == vehiculo["modelo"]:
            return indice
    
    return -1 

def actualizardisponibilidad(lista):

    for vehiculo in lista:
        if vehiculo["año"] >= 2020:
            vehiculo["disponible"] = True
        else:
            vehiculo["disponible"] = False

    print("Se actualizaron los registros de vehiculos")


def mostrarVehiculos(lista):

    if len(lista) == 0:
        print("No existen vehiculos registrados aún")
        return

    actualizardisponibilidad(lista)

    print("=== LISTA DE VEHICULOS ===")
    for vehiculo in lista:
        print(f"Modelo: {vehiculo['modelo']}")
        print(f"Precio: {vehiculo['precio']}")
        print(f"Año: {vehiculo['año']}")

        if vehiculo['disponible']:
            print(f"Disponible?: DISPONIBLE")
        else:
            print(f"Disponible?: NO DISPONIBLE")

listadoVehiculoalmacenado = []

while True:

    mostrarMenu()

    opcion = opcion_menu()

    match opcion:

        case 1:
            agregar_vehiculo(listadoVehiculoalmacenado)
        case 2:
            modeloBuscado = input("Ingresa el modelo a buscar: ")

            posicionVehiculo = buscarVehiculo(listadoVehiculoalmacenado, modeloBuscado)

            if posicionVehiculo >= 0:
                print("")
                print(f"Vehiculo encontrado en la posición {posicionVehiculo}")

                vehiculoEncontrado = listadoVehiculoalmacenado[posicionVehiculo]

                print(f"Modelo: {vehiculoEncontrado['modelo']}")
                print(f"Precio: {vehiculoEncontrado['precio']}")
                print(f"Año: {vehiculoEncontrado['año']}")

                if vehiculoEncontrado['disponible']:
                    print(f"Disponible?: DISPONIBLE")
                    print("")
                else:
                    print(f"Disponible?: NO DISPONIBLE")
                    print("")
            else:
                print(f"Vehiculo {modeloBuscado} no encontrado.")

        case 3:
            modeloBuscado = input("Ingresa el modelo a eliminar: ")

            posicionVehiculo = buscarVehiculo(listadoVehiculoalmacenado, modeloBuscado)

            if posicionVehiculo >= 0:
                listadoVehiculoalmacenado.pop(posicionVehiculo)
                print(f"El vehiculo {modeloBuscado} se ha eliminado.")
            else:
                print(f"El vehiculo { modeloBuscado} no se encuentra registrado.")

        case 4:
          
          actualizardisponibilidad(listadoVehiculoalmacenado)

        case 5:

            mostrarVehiculos(listadoVehiculoalmacenado)
        case 6:
            print("Gracias por usar el sistema. Vuelva Pronto")
            break
        case _:
            print("ERROR: Opción invalida!")
