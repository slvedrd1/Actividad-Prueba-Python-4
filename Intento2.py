def ingresar_usuario(usuario):

    while True:
        nombre = input("Ingrese nombre: ").strip().lower()

        if nombre in usuario:
            print("El nombre ya se encuentra ingresado. ")
        else:
            break

    while True:
        
        sexo = input("Ingrese sexo (F/M): ").strip().upper()

        if (sexo == "F") or (sexo == "M"):
            break
        else:
            print("La opcion debe ser (F/M), intente otra vez.")

    while True:
        contraseña = input("Ingrese contraseña, debe contener Min. 8 caracteres y 1 letra: ")

        if validar_contraseña(contraseña):
            break
        else:
            print("Contraseña invalida, Min 8 caracteres y 1 letra.")


    usuario[nombre] = [sexo,contraseña]
    print("Usuario registrado exitosamente!.")

def buscar_usuario(usuario):

    buscar = input("Ingrese el nombre que desea buscar: ").strip().lower()
    
    if buscar in usuario:
        #para extraer los datos tiene que buscar primero en el diccionario 
        datos = usuario[buscar] 
        print(f"Usuario encontrado: {buscar} / Sexo: {datos[0]} / Contraseña: {datos[1]}")
        #print(f"{usuario[buscar][0]}") otra forma de buscar sin asignar variable
        
    else:
        print("Usuario no registrado.")

def eliminar_usuario(usuario):

    eliminar = input("Ingrese el usuario que desea eliminar: ").strip().lower()

    if eliminar in usuario:
        del usuario[eliminar]
        print(f"Usuario: {eliminar} eliminado.")
        
    else:
        print("Usuario no encontrado.")

def validar_contraseña(contraseña):

    if len(contraseña) < 8:
        return False
    
    if " " in contraseña:
        return False
    
    num = False
    letra = False

    for caracter in contraseña:

        if caracter.isdigit():
            num = True
        if caracter.isalpha():
            letra = True

    return num and letra


usuario = {}

while True:

    print("=== MENÚ ===")
    print("1.- Ingresar Usuario.")
    print("2.- Buscar Usuario.")
    print("3.- Eliminar Usuario.")
    print("4.- Salir.")

    while True:    
        try:
            opcionMenu = int(input("Ingrese una opcion del menu: "))
            break
        except ValueError:
            print("Debe ingresar una opcion valida! (1/4)")

    match opcionMenu:

        case 1:

            ingresar_usuario(usuario)

        case 2:

            buscar_usuario(usuario)

        case 3:

            eliminar_usuario(usuario)

        case 4:
            break

        case _:
            print("Opcion invalida.")
