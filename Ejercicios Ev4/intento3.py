def menu():

    print("=== MENU PRINCIPAL ===")
    print("1. Agregar vehiculo")
    print("2. Buscar vehiculo")
    print("3. Eliminar vehiculo")
    print("4. Actualizar vehiculo")
    print("5. Mostrar vehiculo")
    print("6. Salir")
    print("======================")

def opcion_menu():

    while True:
        try:
            opcionMenu = int(input("Ingrese una opcion del menu: "))
            
            if opcionMenu > 0 and opcionMenu <= 6:
                return opcionMenu
            else:
                print("ERROR: Opcion invalida (1-6)")
        except ValueError:
            print("ERROR: Opcion invalida.")
            

#################################################################
def validar_modelo(modelo):

    if modelo.strip() == "":
        return False
    else:
        return True
    
def validar_año(año):

    try:
        año = int(año)

        if año > 1900:
            return True
        else:
            return False
    except:
        return False
    
def validar_precio(precio):

    try:
        precio = float(precio)

        if precio > 0:
            return True
        else:
            return False
    except:
        return False


def agregar_vehiculo(listaVehiculo):

    modelo = input("Ingrese modelo del vehiculo: ").lower()
    año = input("Ingrese año del vehiculo: ")
    precio = input("Ingrese precio del vehiculo: ")

    modeloValidado = validar_modelo(modelo)
    añoValidado = validar_año(año)
    precioValidado = validar_precio(precio)

    if not modeloValidado:
        print("El modelo no debe estar vacio.")
    if not añoValidado:
        print("El año debe ser un numero entero mayor que 1900.")
    if not precioValidado:
        print("El precio debe ser un numero decimal mayor que 0.")

    if modeloValidado and añoValidado and precioValidado:

        vehiculo = {
            "modelo" : modelo,
            "año" : int(año),
            "precio" : float(precio),
            "disponible" : False
        }

        listaVehiculo.append(vehiculo)
        print("Vehiculo agregado exitosamente!")
        print("")
    else:
        print("ERROR: No se pudo agregar el vehiculo")

def buscar_vehiculo(lista, modelo):

    for indice, vehiculo in enumerate(lista):

        if vehiculo["modelo"] == modelo:
            return indice
    return -1

def actualizar_disponibilidad(lista):

    for vehiculo in lista:

        if vehiculo["año"] >= 2020:
            vehiculo["disponible"] = True
        else:
            vehiculo["disponible"] = False

def mostrar_vehiculos(lista):

    if len(lista) == 0:
        print("No hay vehiculos registrados.")
        return
    
    actualizar_disponibilidad(lista)

    for vehiculo in lista:
        
        estado = "DISPONIBLE" if vehiculo["disponible"] else "NO DISPONIBLE"

        print("=== LISTA DE VEHICULOS ===")
        print(f"Modelo: {vehiculo["modelo"]}")
        print(f"Año: {vehiculo["año"]}")
        print(f"Precio: {vehiculo["precio"]}")
        print(F"Disponible: {estado}")




coleccion_vehiculos = []

while True:

    menu()
    opcion = opcion_menu()

    match opcion:

        case 1:
            agregar_vehiculo(coleccion_vehiculos)
        case 2:
            
            buscar = input("Ingrese vehiculo a buscar: ").lower()
            posicion = buscar_vehiculo(coleccion_vehiculos, buscar)

            if posicion != -1:

                vehiculo = coleccion_vehiculos[posicion]

                print("== DETALLES DEL VEHICULO ==")
                print(f"Modelo : {buscar} / Año : {vehiculo["año"]} / Precio : {vehiculo["precio"]} / Disponible : {vehiculo["disponible"]} ")
                print("")

            else:
                print("Vehiculo no encontrado.")

        case 3:

            eliminar = input("Ingrese el vehiculo que desea eliminar: ").lower()
            posicion = buscar_vehiculo(coleccion_vehiculos, eliminar)

            if posicion != -1:

                coleccion_vehiculos.pop(posicion)
                print(f"Vehiculo: {eliminar} eliminado.")

            else:
                print("El vehiculo no se encuentra registrado.")

        case 4:

            actualizar_disponibilidad(coleccion_vehiculos)
            print("Disponibilidad de vehiculos actualizada!.")

        case 5:
            mostrar_vehiculos(coleccion_vehiculos)

        case 6:
            print("Gracias por usar el sistema. Vuelva Pronto.")
            break
        case _:
            print("ERROR: Opcion invalida")


