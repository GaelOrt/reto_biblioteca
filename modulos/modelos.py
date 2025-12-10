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

    @property
    def id_usuario(self):
        return self._id_usuario

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

    @property
    def id_libro(self):
        return self._id_libro

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

    @property
    def id_prestamo(self):
        return self._id_prestamo

    @property
    def id_libro(self):
        return self._id_libro

    def marcar_devuelto(self):
        """
        Se ha devuelto el préstamo
        """
        self._devuelto = True
        self._fecha_fin = datetime.now()

    def __str__(self):
        """
        Se muestra el prestamo

        Returns:
        list: Texto con los datos del prestamo
        """
        return f'Id Libro: {self._id_libro}, Id Usuario: {self._id_usuario}, Fecha Inicio: {self._fecha_inicio}, Fecha Fin: {self._fecha_fin}, Devuelto: {self._devuelto}'


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
        if usuarios is None:
            usuarios = []
        self._usuarios = usuarios
        if prestamos is None:
            prestamos = []
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
        return libro

    def registrar_usuario(self, nombre, tipo):
        """
        Se reguistra el usuario

        Args:
        nombre (str): Nombre del usuario
        tipo (str): Tipo de usuario
        """
        usuario = Usuario(nombre, tipo, len(self._usuarios))

        self._usuarios.append(usuario)
        return usuario

    def prestar_libro(self, id_libro, id_usuario):
        """
        Se presta el libro

        Args:
        id_libro (str): Id del libro
        id_usuario (str): Id del usuario
        """
        prestamo = Prestamo(id_libro, id_usuario)

        self._prestamos.append(prestamo)
        print(f'Se ha prestado el libro al usuario: {prestamo}')

    def devolver_libro(self, id_prestamo):
        """
        Se devuelve el libro

        Args:
        id_prestamo (str): Id del préstamo
        """
        id_li = None
        for prestamo in self._prestamos:
            if prestamo.id_prestamo == id_prestamo:
                id_li = prestamo.id_libro
                prestamo.marcar_devuelto()

        if id_li is None:
            print('No se ha encontrado el préstamo')
            return

        for libro in self._libros:
            if libro.id_libro == id_li:
                libro.marcar_devuelto()
        print(f'Se ha ha devuelto el prestamo')

    def listar_libros(self):
        if not self._libros:
            print('No hay libros almacenados')
            return None

        print('Libros:')
        for indx, l in enumerate(self._libros):
            print(f'{indx + 1}. {l}')
        return self._libros

    def listar_usuarios(self):
        if not self._usuarios:
            print('No hay usuarios almacenados')
            return None

        print('Usuarios:')
        for indx, u in enumerate(self._usuarios):
            print(f'{indx + 1}. {u}')
        return self._usuarios

    def listar_prestamos(self):
        if not self._prestamos:
            print('No hay prestamos almacenados')
            return None

        print('Prestamos:')
        for indx, p in enumerate(self._prestamos):
            print(f'{indx + 1}. {p}')
        return self._prestamos

    def to_dict(self):
        return
