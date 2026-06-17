#validaciones para agregar
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


#funciones para entrar al menu
def menu():

    print("====== MENÚ PRINCIPAL ======")
    print("1. Agregar Vehiculo.")
    print("2. Buscar vehiculo")
    print("3. Eliminar vehiculo")
    print("4. Actualizar disponibilidad")
    print("5. Mostrar vehiculos")
    print("6. Salir")
    print("============================")

def opcionMenu():

    while True:
        try:
            opcion = int(input("Ingrese una opcion del menú: "))

            if opcion > 0 and opcion <= 6:
                return opcion
            else:
                print("ERROR: Opcion invalida (1-6).")
        except ValueError:
            print("ERROR: Debe ingresar un valor numerico.")

#funciones de las opciones

def agregar_vehiculo(listaVehiculo):
    
    modelo = input("Ingrese modelo del vehiculo: ")
    anio = input("Ingrese anio del vehiculo: ")
    precio = input("Ingrese precio del vehiculo: ")

    modeloValidado = validar_modelo(modelo)
    anioValidado = validar_anio(anio)
    precioValidado = validar_precio(precio)

    if not modeloValidado:
        print("El modelo no puede estar vacio.")
    if not anioValidado:
        print("El año debe ser un numero entero mayor que 1900.")
    if not precioValidado:
        print("El precio debe ser un numero decimal mayor que 0.")

    if modeloValidado and anioValidado and precioValidado:

        vehiculo = {
            "modelo" : modelo,
            "anio" : int(anio),
            "precio" : float(precio),
            "disponible" : False
        }

        listaVehiculo.append(vehiculo)
        print("Vehiculo agregado exitosamente!")
    else:
        print("No se pudo agregar el vehiculo.")

def buscar_vehiculo(lista, modelo):

    # Enumerate nos da el índice y el vehículo en cada vuelta
    for indice, vehiculo in enumerate(lista):
        if vehiculo["modelo"] == modelo:
            return indice
    return -1

def actualizar_disponibilidad(lista):

    for vehiculos in lista:
        
        if vehiculos["anio"] >= 2020:
            vehiculos["disponible"] = True
            
        else:
            vehiculos["disponible"] = False
            

def mostrar_vehiculos(lista):
    
    if len(lista) == 0:
        print("No hay registros en el concesionario.")
        return
    
    actualizar_disponibilidad(lista)

    for vehiculos in lista:

        estado = "DISPONIBLE" if vehiculos["disponible"] else "NO DISPONIBLE"

        print(f"{vehiculos["modelo"]} / {vehiculos["anio"]} / {vehiculos["precio"]} / Disponible: {estado}")
        

coleccion_vehiculos = []

while True:

    menu()
    opcion = opcionMenu()
    
    match opcion: 
        
        case 1:
            agregar_vehiculo(coleccion_vehiculos)
        case 2:

            buscar = input("Ingrese el modelo a buscar: ")
            posicion = buscar_vehiculo(coleccion_vehiculos, buscar)

            if posicion != -1:

                vehiculo = coleccion_vehiculos[posicion]

                print("=== VEHICULO ENCONTRADO ===")
                print(f"Posicion: {posicion} / Vehiculo: {buscar} / Precio: {vehiculo["precio"]} / Anio: {vehiculo["anio"]} / Disponible: {vehiculo["disponible"]}")
                print("")

            else:
                print("Vehiculo no encontrado.")

        case 3:

            eliminar = input("Ingrese el modelo que desea eliminar: ")
            posicion = buscar_vehiculo(coleccion_vehiculos, eliminar)

            if posicion != -1:
                
                #pop elimina el indice
                coleccion_vehiculos.pop(posicion)
                print(f"Vehiculo {eliminar} eliminado correctamente!.")

            else:
                print(f"El vehiculo {eliminar} no se encuentra registrado. ")

        case 4:
            actualizar_disponibilidad(coleccion_vehiculos)
        case 5:
            mostrar_vehiculos(coleccion_vehiculos)
        case 6:
            print("Gracias por usar el sistema. Vuelva Pronto")
            break
        case _:
            print("ERROR: Opcion invalida!")




            



    
    
