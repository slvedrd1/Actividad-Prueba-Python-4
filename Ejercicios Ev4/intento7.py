#----------------- FUNCION MENU Y OPCION ----------------------------

def menu():

    print("======== MENU PRINCIPAL ========")
    print("1. Agregar vehiculo")
    print("2. Buscar vehiculo")
    print("3. Eliminar vehiculo")
    print("4. Actualizar vehiculo")
    print("5. Mostrar vehiculo")
    print("6. Salir")
    print("================================")

def opcion_menu():

    while True:
        try:
            opcion = int(input("Ingrese una opcion del menu: "))
            return opcion
        except ValueError:
            print("ERROR: Debe ingresar una opcion disponible (1-6)")

#-------------------- VALIDACIONES OPCION 1 ---------------------------

def validar_modelo(modelo):

    if modelo.strip() == "":
        return False
    else:
        return True
    
def validar_anio(anio):

    try:
        anio = int(anio)

        if anio > 1900:
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
    
#------------------------ FUNCIONES DEL MENU ---------------------------

def agregar_vehiculo(listavehiculo):

    modelo = input("Ingrese el modelo del vehiculo: ").title()
    anio = input("Ingrese año del vehiculo: ")
    precio = input("Ingrese precio del vehiculo: ")

    modelovalidado = validar_modelo(modelo)
    aniovalidado = validar_anio(anio)
    preciovalidado = validar_precio(precio)

    if not modelovalidado:
        print("El modelo no puede quedar vacio.")
    if not aniovalidado:
        print("El año debe ser mayor que 1900.")
    if not preciovalidado:
        print("El precio debe ser mayor que 0.")

    if modelovalidado and aniovalidado and preciovalidado:

        vehiculo = {
            "modelo" : modelo,
            "anio" : int(anio),
            "precio" : float(precio),
            "disponible" : False
        }
        
        listavehiculo.append(vehiculo)
        print("---- VEHICULO AGREGADO EXITOSAMENTE ---")
        print("")

    else:
        print("--- No se pudo agregar el vehiculo! ---")

def buscar_vehiculo(lista, modelo):

    for indice, vehiculo in enumerate(lista):

        if vehiculo["modelo"] == modelo:
            return indice
    return -1

def actualizar_vehiculo(lista):

    for vehiculo in lista:

        if vehiculo["anio"] >= 2020:
            vehiculo["disponible"] = True
        else:
            vehiculo["disponible"] = False

def mostrar_vehiculo(lista):

    if len(lista) == 0:
        print("No hay vehiculos registrados.")
        return
    
    actualizar_vehiculo(lista)

    for vehiculo in lista:

        estado = "DISPONIBLE" if vehiculo["disponible"] else "NO DISPONIBLE"

        print(f"Modelo: {vehiculo["modelo"]}")
        print(f"Año: {vehiculo["anio"]}")
        print(f"Precio: {vehiculo["precio"]}")
        print(f"Disponibilidad: {estado}")
        print("==============================")

coleccion_vehiculos = []

while True:

    menu()
    opcionMenu = opcion_menu()

    match opcionMenu:

        case 1:
            agregar_vehiculo(coleccion_vehiculos)

        case 2:
            buscar = input("Ingrese el nombre del vehiculo a buscar: ").title()
            posicion = buscar_vehiculo(coleccion_vehiculos, buscar)

            if posicion != -1:
                actualizar_vehiculo(coleccion_vehiculos)

                v = coleccion_vehiculos[posicion]

                estado = "DISPONIBLE" if v["disponible"] else "NO DISPONIBLE"

                print("--- VEHICULO ENCONTRADO! ---")
                print(f"Posicion: {posicion} /Modelo: {v["modelo"]} /Año: {v["anio"]} /Precio: {v["precio"]} /Disponible: {estado}")
                print("")

            else:
                print(f"--- Vehiculo {buscar} no encontrado! ---")
                print("")

        case 3:
            eliminar = input("Ingrese el vehiculo que desea eliminar: ").title()
            posicion = buscar_vehiculo(coleccion_vehiculos, eliminar)

            if posicion != -1:

                coleccion_vehiculos.pop(posicion)
                print(f"--- Vehiculo {eliminar} eliminado exitosamente ---")
                print("")

            else:
                print(f"--- El vehiculo {eliminar} no se encuentra registrado ---")
                print("")

        case 4: 
            actualizar_vehiculo(coleccion_vehiculos)
            print("--- DISPONIBILIDAD ACTUALIZADA! ---")

        case 5:
            print("---- VEHICULOS ----")
            mostrar_vehiculo(coleccion_vehiculos)

        case 6:
            print("Gracias por usar el sistema. Vuelva Pronto")
            break
        case _:
            print("ERROR: Debe ingresar una opcion disponible (1-6)")


  


