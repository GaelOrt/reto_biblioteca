from .modelos import *
from .validaciones import *
from pathlib import Path
from .persistencia import *


def obtener_biblioteca():
    """
    Función para la carga de al biblioteca.
    """
    json_file = Path().cwd() / 'biblioteca.json'
    pickle_file = Path().cwd() / 'biblioteca.pkl'
    gjson = GestorPersistencia(EstrategiaJSON())

    if not json_file.exists() and not pickle_file.exists():
        bib = Biblioteca()
        gjson.guardar(bib)
        return bib
    elif json_file.exists():
        return gjson.cargar()
    else:
        gpickle = GestorPersistencia(EstrategiaPickle())
        return gpickle.cargar()


def agregar_libro(biblioteca: Biblioteca):
    """
    Función para añadir libros a la biblioteca.

    Args:
    biblioteca (Biblioteca): Objeto con libros, usuarios y prestamos.
    """
    titulo = input_str('Introduce el titulo del libro: ')
    autor = input_str('Introduce el autor del libro: ')
    anio = input_int('Introduce el año de salida del libro: ', 0, 2025)

    libro = biblioteca.registrar_libro(titulo, autor, anio)
    print(f'Se ha agregado el libro: {libro}')


def agregar_usuario(biblioteca: Biblioteca):
    """
     Función para añadir usuarios a la biblioteca.

     Args:
     biblioteca (Biblioteca): Objeto con libros, usuarios y prestamos.
     """
    nombre = input_str('Introduce el nombre del usuario: ')
    tipo = input_str('Introduce el tipo del usuario (admin/user): ')

    usuario = biblioteca.registrar_usuario(nombre, tipo)
    print(f'Se ha agregado el usuario: {usuario}')


def prestar_libro(biblioteca: Biblioteca):
    """
     Función para cambiar el estado de un libro de la biblioteca.

     Args:
     biblioteca (Biblioteca): Objeto con libros, usuarios y prestamos.
     """
    libros = biblioteca.listar_libros()
    if not libros:
        return

    libro_index = input_int('Introduce el numero del libro que desees prestar: ', 1, len(libros))
    libro_find = libros[libro_index - 1]

    usuarios = biblioteca.listar_usuarios()

    if not usuarios:
        return

    usuario_index = input_int('Introduce el numero del usuario al que se le presta el libro: ', 1, len(usuarios))
    usuario_find = usuarios[usuario_index - 1]

    biblioteca.prestar_libro(libro_find.id_libro, usuario_find.id_usuario)
    libro_find.marcar_prestado()


def devolver_libro(biblioteca: Biblioteca):
    """
     Función para cambiar el estado de un libro de la biblioteca.

     Args:
     biblioteca (Biblioteca): Objeto con libros, usuarios y prestamos.
     """
    prestamos = biblioteca.listar_prestamos()
    if not prestamos:
        return

    for p in prestamos:
        if not p.devuelto:
            break
    else:
        print('Los prestamos existentes ya han sido devueltos')
        return

    prestamos_index = input_int('Introduce el numero del prestamos que pretendas devolver: ', 1, len(prestamos))
    prestamo_find = prestamos[prestamos_index - 1]

    if prestamo_find.devuelto:
        print('Este prestamo ya ha sido devuelto')
        return

    biblioteca.devolver_libro(prestamo_find.id_prestamo)
    print(prestamo_find)
