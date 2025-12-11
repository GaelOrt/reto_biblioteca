from modulos import *


def mostrar_menu(opciones):
    """
    Mostrar menu principal de la app

    Parameters:
    opciones (list): Opciones a mostrar

    Returns:
    int: Índice de la opción que se ha elegido
    """
    for x in opciones:
        print(x)
    return input_int('Opción del menu: ', 0, len(opciones) - 1)


def main():
    """
    Función raiz de la App
    """
    b = obtener_biblioteca()
    gjson = GestorPersistencia(EstrategiaJSON())
    gpickle = GestorPersistencia(EstrategiaPickle())

    while True:
        print('\n')
        match mostrar_menu(
            ['1. Listar libros.',
             '2. Registrar nuevo libro.',
             '3. Registrar usuario.',
             '4. Prestar libro.',
             '5. Devolver libro',
             '6. Guardar (JSON)',
             '7. Guardar (pickle)',
             '8. Cargar (JSON)',
             '9. Cargar  (pickle)',
             '0. Salir']):
            case 1:
                b.listar_libros()
            case 2:
                agregar_libro(b)
            case 3:
                agregar_usuario(b)
            case 4:
                prestar_libro(b)
            case 5:
                devolver_libro(b)
            case 6:
                gjson.guardar(b)
            case 7:
                gpickle.guardar(b)
            case 8:
                b = gjson.cargar()
            case 9:
                b = gpickle.cargar()
            case 0:
                print('Saliendo...')
                break
            case _:
                print('Opción no aceptada')


if __name__ == '__main__':
    main()
