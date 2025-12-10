from .modelos import *
from .validaciones import *


def obtener_biblioteca():
    return Biblioteca()


def agregar_libro(biblioteca: Biblioteca):
    titulo = input_str('Introduce el titulo del libro: ')
    autor = input_str('Introduce el autor del libro: ')
    anio = input_int('Introduce el año de salida del libro: ', 0, 2025)

    libro = biblioteca.registrar_libro(titulo, autor, anio)
    print(f'Se ha agregado el libro: {libro}')


def agregar_usuario(biblioteca: Biblioteca):
    nombre = input_str('Introduce el nombre del usuario: ')
    tipo = input_str('Introduce el tipo del usuario (admin/user): ')

    usuario = biblioteca.registrar_usuario(nombre, tipo)
    print(f'Se ha agregado el usuario: {usuario}')


def prestar_libro(biblioteca: Biblioteca):
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
    prestamos = biblioteca.listar_prestamos()

    if not prestamos:
        return

    prestamos_index = input_int('Introduce el numero del prestamos que pretendas devolver: ', 1, len(prestamos))
    prestamo_find = prestamos[prestamos_index - 1]

    biblioteca.devolver_libro(prestamo_find.id_prestamo)
    print(prestamo_find)
