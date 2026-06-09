def ingresar_usuario(usuario):

    while True:
       
        nombre = input("Ingrese nombre de usuario: ").strip().lower()
        
        if nombre in usuario:
            print("El nombre de usuario no puede estar repetido.")
        else:
            print("Usuario ingresado con exito.")
            break

    while True:

        sexo = input("Ingrese sexo (F/M): ").strip().upper()

        if (sexo == "M") or (sexo == "F"):
            print("Sexo registrado correctamente.")
            break
        else:
             print("Error, el sexo debe ser (F/M).")

    while True:

        contraseña = input("Ingrese contraseña, (Min 8 caracteres y debe contener 1 letra.): ")
        
        if " " in contraseña:
            print("No debe contener espacios.")
        elif len(contraseña) < 8:
            print("Debe tener un minimo de 8 caracteres")
        else:

            tiene_letra = False
            tiene_numero = False

            for caracter in contraseña:

                if caracter.isdigit():
                    tiene_numero = True
                elif caracter.isalpha():
                    tiene_letra = True

            if (tiene_letra == True) and (tiene_numero == True):
                print("Contraseña valida.")
                break
            else:
                print("Contraseña invalida, debe contener al menos un numero y una letra.")

    usuario[nombre] = [sexo, contraseña]
    print("Usuario ingresado correctamente.")

def buscar_usuario(usuario):

    if len(usuario) == 0:
        print("No se encuentran usuarios registrados.")
        return

    buscar = input("Ingrese el usuario que desea buscar: ").lower()

    if buscar in usuario:

        datos = usuario[buscar]
        print(f"Usuario encontrado: {buscar} / Sexo: {datos[0]} / Contraseña: {datos[1]}")
    else:
        print("Usuario no encontrado.")

def eliminar_usuario(usuario):

    if len(usuario) == 0:
        print("No se encuentran usuarios registrados.")
        return
    
    eliminar = input("Ingrese al usuario que desea eliminar: ").strip().lower()

    if eliminar in usuario:
        del(usuario[eliminar])
        print("Usuario eliminado.")
    else:
        print("No se pudo eliminar usuario!")