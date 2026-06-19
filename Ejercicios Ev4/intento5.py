#----------------------- MENUUUUUUUUUUUU

def menu():

    print("=== MENU PRINCIPAL ===")
    print("1. Agregar productos.")
    print("2. Buscar productos")
    print("3. Eliminar productos")
    print("4. Actualizar disponibilidad")
    print("5. Mostrar vehiculos")
    print("6. Salir")
    print("=====================")

def menu_opciones():

    while True:
        try:
            opcion = int(input("Ingrese opcion del menu: "))

            if opcion > 0 and opcion <= 6:
                return opcion
            else:
                print("ERROR: Opcion invalida!")
        except ValueError:
            print("ERROR: Debe ingresar una opcion valida.")

#--------------------------- VALIDACIONES OPCION 1

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

#----------------------------------- FUNCIONES MENU PRINCIPAL

def agregar_productos(almacen):

    modelo = input("Ingresar modelo del vehiculo: ").title()
    anio = input("Ingrese anio del vehiculo: ")
    precio = input("Ingrese precio del vehiculo: ")

    modeloValidado = validar_modelo(modelo)
    anioValidado = validar_anio(anio)
    precioValidado = validar_precio(precio)

    if not modeloValidado:
        print("El nombre no debe quedar vacio.")
    if not anioValidado:
        print("El año debe ser mayor que 1900")
    if not precioValidado:
        print("El precio debe ser mayor que 0.")

    if modeloValidado and anioValidado and precioValidado:

        nuevosProductos = {
            "modelo" : modelo,
            "anio" : int(anio),
            "precio" : float(precio),
            "disponible" : False
        }

        almacen.append(nuevosProductos)
        print("Ingreso de datos éxitoso!")
        print("")

    else:
        print("No se pudo agregar los datos.")
        print("")

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

def mostrar_vehiculos(lista):

    if len(lista) == 0:
        print("No hay vehiculos registrados")
        return
    
    actualizar_vehiculo(lista)

    print("---- MOSTRAR VEHICULOS ----")

    for vehiculo in lista:

        estado = "DISPONIBLE" if vehiculo["disponible"] else "NO DISPONIBLE"

        print(f"Modelo: {vehiculo["modelo"]}")
        print(f"Anio: {vehiculo["anio"]}")
        print(f"Precio: {vehiculo["precio"]}")
        print(f"Disponible: {estado}")
        print("")


coleccion_general = []

while True:

    menu()
    opcionMenu = menu_opciones()

    match opcionMenu:

        case 1:
            agregar_productos(coleccion_general)
        case 2:

            buscar = input("Ingrese el vehiculo que desea buscar: ").title()
            posicion = buscar_vehiculo(coleccion_general, buscar)

            if posicion != -1:

                vehiculo = coleccion_general[posicion]

                print("---- VEHICULO ENCONTRADO ----")
                print(f"Modelo: {buscar} /Anio: {vehiculo["anio"]} /Precio: {vehiculo["precio"]} /Disponible: {vehiculo["disponible"]}")
            
            else:
                print("Vehiculo no encontrado.")

        case 3:

            eliminar = input("Ingrese vehiculo a eliminar: ").title()
            posicion = buscar_vehiculo(coleccion_general, eliminar)

            if posicion != -1:

                coleccion_general.pop(posicion)
                print("Vehiculo eliminado exitosamente.")

            else:
                print("Vehiculo no encontrado")

        case 4:
            actualizar_vehiculo(coleccion_general)
            print("--- VEHICULOS ACTUALIZADOS! ---")

        case 5:
            mostrar_vehiculos(coleccion_general)
        case 6:
            print("Saliendoo..")
            break
        case _:
            print("ERROR: Opcion invalida!")

                                


