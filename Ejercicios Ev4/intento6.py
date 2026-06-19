#----------------------- FUNCION MENU Y OPCION ------------------------
def menu():

    print("========== MENU PRINCIPAL ==========")
    print("1. Agregar vehiculo")
    print("2. Buscar vehiculo")
    print("3. Eliminar vehiculo")
    print("4. Actualizar vehiculo")
    print("5. Mostrar vehiculo")
    print("6. Salir")
    print("===================================")

def opcion_menu():

    while True:
        try:
            opcion = int(input("Ingrese una opción del menú: "))
            return opcion
        except ValueError:
            print("ERROR: Opción invalida! (1-6)")

#------------------ VALIDACIONES OPCION 1 -------------------------------

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
    
#----------------------- FUNCIONES MENU PRINCIPAL -----------------------

def agregar_vehiculo(listavehiculo):

    modelo = input("Ingrese modelo del vehiculo: ").title()
    anio = input("Ingrese año del vehiculo: ")
    precio = input("Ingrese precio del vehiculo: ")

    modelovalidado = validar_modelo(modelo)
    aniovalidado = validar_anio(anio)
    preciovalidado = validar_precio(precio)

    if not modelovalidado:
        print("El nombre no puede quedar vacio.")
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
        print("--- VEHICULO AGREGADO ÉXITOSAMENTE! ---")
        print("")

    else:
        print("ERROR: No se pudo agregar el vehiculo!")

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
        print("No hay vehiculos registrados!")
        return
    
    actualizar_vehiculo(lista)

    for vehiculo in lista:

        estado = "DISPONIBLE" if vehiculo["disponible"] else "NO DISPONIBLE"

        print(f"Modelo: {vehiculo["modelo"]}")
        print(f"Año: {vehiculo["anio"]}")
        print(f"Precio: {vehiculo["precio"]}")
        print(f"Disponibilidad: {estado}")
    
#----------------- MAIN MENU -----------------------------------------------

coleccion_vehiculo = []

while True:

    menu()
    opcionMenu = opcion_menu()

    match opcionMenu:

        case 1:
            agregar_vehiculo(coleccion_vehiculo)
        case 2:
            buscar = input("Ingrese el vehiculo a buscar: ").title()
            posicion = buscar_vehiculo(coleccion_vehiculo, buscar)

            if posicion != -1:
                actualizar_vehiculo(coleccion_vehiculo)

                v = coleccion_vehiculo[posicion]

                estado = "DISPONIBLE" if v["disponible"] else "NO DISPONIBLE"

                print(f"--- VEHICULO ENCONTRADO ---")
                print(f"Posicion: {posicion} /Modelo: {v["modelo"]} /Año: {v["anio"]} /Precio: {v["precio"]} /Disponible: {estado}")
                print("")
            else:
                print(f"Vehiculo {buscar} no encontrado!")

        case 3:
            eliminar = input("Ingrese el vehiculo a eliminar: ").title()
            posicion = buscar_vehiculo(coleccion_vehiculo, eliminar)

            if posicion != -1:
                coleccion_vehiculo.pop(posicion)
                print(f"--- Vehiculo {eliminar} eliminado éxitosamente! ---")
                print("")

            else:
                print(f"El vehiculo {eliminar} no se encuentra registrado")

        case 4:
            actualizar_vehiculo(coleccion_vehiculo)
            print("--- DISPONIBILIDAD ACTUALIZADA! ---")
            print("")
        
        case 5:
            print("--- VEHICULOS REGISTRADOS ---")
            mostrar_vehiculo(coleccion_vehiculo)

        case 6:
            print("Gracias por usar el sistema. Vuelva Pronto")
            break
        case _:
            print("ERROR: Opcion invalida (1-6)")
            


