def agregar_producto(inventario):

    nombre = validar_nombre()
    precio = validar_precio()
    stock = validar_stock()

    productos = {
        "nombre" : nombre,
        "precio" : precio,
        "stock" : stock,
        "disponible" : False
    }
    
    inventario.append(productos)

def buscar_producto(inventario):

    buscar = input("Ingrese el nombre del producto que desea buscar: ").strip().lower()

    encontrar = False

    for productos in inventario:

        if productos ["nombre"] == buscar:
            print(f"Producto: {buscar} / Precio: {productos["precio"]} / Stock: {productos["stock"]}")
            encontrar = True
            break
    
    if not encontrar:
        print("Producto no encontrado.")

def eliminar_producto(inventario):

    eliminar = input("Que producto desea eliminar: ").strip().lower()

    encontrar = False

    # Usamos range(len(inventario)) para tener acceso al número de posición (i)
    for i in range(len(inventario)):
       
        # Accedemos al producto usando el índice [i]
        if inventario[i]["nombre"] == eliminar:

            del inventario[i]
            print(f"Producto eliminado correctamente: {eliminar}")
            encontrar =  True
            break

    if not encontrar:
        print("Producto no encontrado.")

def actualizar_disponibilidad(inventario):

    nombre = input("Que producto desea cambiar la disponibilidad: ").strip().lower()

    encontrar = False

    for productos in inventario:

        if productos["nombre"] == nombre:

            productos["disponible"] = not productos["disponible"]
            print(f"Producto: {productos["nombre"]} / Su disponibilidad es: {productos["disponible"]}")
            
            encontrar = True
            break

    if not encontrar:
        print("Producto no encontrado.")

def mostrar_producto(inventario):

    if len(inventario) == 0:
        print("Inventario vacio.")
    else:
        print("== Inventario Actual ==")
       
        estado = " "

        for productos in inventario:

            if productos["disponible"] == True:
                estado = "Disponible"
            else:
                estado = "No disponible" 

            print(f"Producto: {productos["nombre"]} / Precio: {productos["precio"]} / Stock: {productos["stock"]} / Disponibilidad: {estado}")
                
                
            


def validar_nombre():

    while True:
        nombre = input("Ingrese nombre del producto: ").strip().lower()

        if nombre:
            return nombre
        else:
            print("El nombre no debe quedar vacio.")
    
def validar_precio():

    while True:
        try:
            precio = float(input("Ingrese precio: "))

            if precio > 0:
                return precio
            else:
                print("El precio debe ser mayor a 0.")
        except ValueError:
            print("Error: El valor debe ser numerico.")

def validar_stock():

    while True:
        try:
            stock = int(input("Ingrese el stock: "))

            if stock >= 0:
                return stock
            else:
                print("El stock no puede ser menor que 0.")
        except ValueError:
            print("Error: El valor debe ser numerico.")


inventario = []

while True:

    print("=== MENÚ PRINCIPAL ===") 
    print("1. Agregar Produto")
    print("2. Buscar Producto")
    print("3. Eliminar Producto")
    print("4. Actualizar Disponibilidad")
    print("5. Mostrar Producto")
    print("6. Salir")

    try:
        opcionMenu = int(input("Ingrese una opcion del menu: "))
    except ValueError:
        print("Error, opción inválida!")
        continue

    match opcionMenu:

        case 1:
            agregar_producto(inventario)
        case 2:
            buscar_producto(inventario)
        case 3:
            eliminar_producto(inventario)
        case 4:
            actualizar_disponibilidad(inventario)
        case 5:
            mostrar_producto(inventario)
        case 6:
            print("Cerrando..")
            break
        case _:
            print("Error: Opcion invalida!")

