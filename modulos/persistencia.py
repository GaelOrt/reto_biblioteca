import json
import pickle
from datetime import datetime
from abc import ABC, abstractmethod
from .modelos import *


class GestorPersistencia:
    def __init__(self, estrategia):
        self.estrategia = estrategia

    def guardar(self, biblioteca):
        self.estrategia.guardar(biblioteca)

    def cargar(self):
        return self.estrategia.cargar()


class EstrategiaPersistencia(ABC):
    @abstractmethod
    def guardar(self, biblioteca):
        raise NotImplementedError

    @abstractmethod
    def cargar(self):
        raise NotImplementedError


class EstrategiaJSON(EstrategiaPersistencia):
    def guardar(self, biblioteca):
        """
         Función para guardar la biblioteca en JSON.

         Args:
         biblioteca (Biblioteca): Objeto con libros, usuarios y prestamos.
         """
        try:
            with open("biblioteca.json", "w", encoding="utf-8") as f:
                json.dump(biblioteca, f, indent=4, ensure_ascii=False, cls=MiEncoder)

        except FileNotFoundError:
            print("El archivo no existe.")

        except PermissionError:
            print("No tienes permiso para leer este archivo.")

    def cargar(self):
        """
         Función para cargar la biblioteca del JSON.
         """
        try:
            with open("biblioteca.json") as f:
                diccionario = json.load(f, object_hook=decodificar_biblioteca)

            return diccionario

        except FileNotFoundError:
            print("El archivo no existe.")

        except PermissionError:
            print("No tienes permiso para leer este archivo.")

        except json.JSONDecodeError as e:
            print(f"JSON mal formado: {e}")


class EstrategiaPickle(EstrategiaPersistencia):
    def guardar(self, biblioteca):
        """
         Función para guardar la biblioteca en JPickle.

         Args:
         biblioteca (Biblioteca): Objeto con libros, usuarios y prestamos.
         """
        try:
            with open("biblioteca.pkl", "wb") as f:
                pickle.dump(biblioteca, f)

        except FileNotFoundError:
            print("El archivo no existe.")

        except PermissionError:
            print("No tienes permiso para leer este archivo.")

    def cargar(self):
        """
         Función para cargar la biblioteca del JPickle.
         """
        try:
            with open("biblioteca.pkl", "rb") as f:
                biblio = pickle.load(f)
                return biblio

        except FileNotFoundError:
            print("El archivo no existe.")

        except PermissionError:
            print("No tienes permiso para leer este archivo.")

        except pickle.UnpicklingError:
            print("Archivo dañado o corrupto.")

        except EOFError:
            print("Archivo incompleto o vacio.")


# Codificador
class MiEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.isoformat()

        if isinstance(obj, Biblioteca):
            return {
                '_libros': obj.libros,
                '_usuarios': obj.usuarios,
                '_prestamos': obj.prestamos
            }

        if isinstance(obj, (Libro, Usuario, Prestamo)):
            return obj.__dict__

        return super().default(obj)


# Decodificador
def decodificar_biblioteca(dic):
    if "_id_prestamo" in dic:
        return Prestamo(dic["_id_libro"], dic["_id_usuario"], dic['_id_prestamo'], dic['_fecha_inicio'],
                        dic['_fecha_fin'], dic['_devuelto'])

    elif "_id_usuario" in dic:
        return Usuario(dic["_nombre"], dic['_tipo'], dic['_id_usuario'])

    elif "_titulo" in dic:
        return Libro(
            dic["_titulo"],
            dic["_autor"],
            dic["_anio"],
            dic['_id_libro'],
            dic['_disponible']
        )

    elif "_libros" in dic and "_usuarios" in dic:
        return Biblioteca(dic['_libros'], dic['_usuarios'], dic['_prestamos'])

    return dic
