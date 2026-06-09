import Funciones as fn

usuario = {}

while True:

    print("=== MENU ===")
    print("1.- Ingresar usuario.")
    print("2.- Buscar usuario.")
    print("3.- Eliminar usuario.")
    print("4.- Salir.")

    try:
        opcionMenu = int(input("Ingrese una opcion del menu: "))
    except ValueError:
        print("Debe ingresar una opción válida!!")
        continue


    match opcionMenu:

        case 1:
            fn.ingresar_usuario(usuario)

        case 2:
            fn.buscar_usuario(usuario)

        case 3:
            fn.eliminar_usuario(usuario)

        case 4:
            print("Programa terminado...")
            break
        case _:
            print("Debe ingresar una opción válida!!")