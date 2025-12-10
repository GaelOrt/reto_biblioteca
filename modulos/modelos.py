from datetime import *


class Usuario:
    """
    Clase con toda la información de un usuario.

    Args:
    nombre (str): Nombre del usuario
    tipo (str): Tipo de usuario
    cantidad (int): Cantidad de usuarios creados

    """

    def __init__(self, nombre, tipo, cantidad=0):
        self._id_usuario = f'U{str(cantidad + 1).zfill(3)}'
        self._nombre = nombre
        self._tipo = tipo

    def __str__(self):
        """
        Se muestra el usuario

        Returns:
        list: Texto con los datos del usuario
        """
        return f'Id: {self._id_usuario}, Nombre: {self._nombre}, Tipo: {self._tipo}'


class Libro:
    """
    Clase con toda la información del libro.

    Args:
    titulo (str): Nombre del usuario
    autor (str): Autor del libro
    anio (int): Año de salida
    disponible (bool): Está disponible el libro / No está prestado
    cantidad (int): Cantidad de libros creados
    """

    def __init__(self, titulo, autor, anio, cantidad=0):
        self._id_libro = f'L{str(cantidad + 1).zfill(3)}'
        self._titulo = titulo
        self._autor = autor
        self._anio = anio
        self._disponible = True

    def marcar_prestado(self):
        """
        Se marca el libro como no disponible
        """
        self._disponible = False

    def marcar_devuelto(self):
        """
        Se marca el libro como disponible
        """
        self._disponible = True

    def __str__(self):
        """
        Se muestra el usuario

        Returns:
        list: Texto con los datos del usuario
        """
        return f'Id: {self._id_libro}, Titulo: {self._titulo}, Autor: {self._autor}, Año: {self._anio}, Disponible: {self._disponible}'


class Prestamo:
    """
    Clase con toda la información del préstamo.

    Args:
    id_libro (str): ID del libro prestado
    id_usuario (str): ID del usuario al que se le ha prestado
    fecha_inicio (int): Fecha de inicio del préstamo
    fecha_fin (int): Fecha de devolución del préstamo
    devuelto (bool): Está devuelto el préstamo
    cantidad (int): Cantidad de libros creados
    """

    def __init__(self, id_libro, id_usuario, cantidad=0):
        self._id_prestamo = f'P{str(cantidad + 1).zfill(3)}'
        self._id_libro = id_libro
        self._id_usuario = id_usuario
        self._fecha_inicio = datetime.now()
        self._fecha_fin = None
        self._devuelto = False

    def marcar_devuelto(self):
        """
        Se ha devuelto el préstamo
        """
        self._devuelto = True
        self._fecha_fin = datetime.now()


class Biblioteca:
    """
    Clase con toda la información de la biblioteca.

    Args:
    _libros (list): Lista de libros
    _usuarios (list): Lista de usuarios
    _prestamos (list): Lista de préstamos
    """

    def __init__(self, libros=None, usuarios=None, prestamos=None):
        if libros is None:
            libros = []
        self._libros = libros
        self._usuarios = usuarios
        self._prestamos = prestamos

    def registrar_libro(self, titulo, autor, anio):
        """
        Se reguistra el libro

        Args:
        titulo (str): titulo del libro
        autor (str): Nombre del autor
        anio (int): Año de salida
        """
        libro = Libro(titulo, autor, anio, len(self._libros))

        self._libros.append(libro)

    def registrar_usuario(self, nombre, tipo):
        """
        Se reguistra el usuario

        Args:
        nombre (str): Nombre del usuario
        tipo (str): Tipo de usuario
        """
        usuario = Usuario(nombre, tipo, len(self._usuarios))

        self._usuarios.append(usuario)

    def prestar_libro(self, id_libro, id_usuario):
        """
        Se prestar el libro

        Args:
        id_libro (str): titulo del libro
        autor (str): Nombre del autor
        anio (int): Año de salida
        """
        libro = Libro(titulo, autor, anio, len(self._libros))

        self._libros.append(libro)
