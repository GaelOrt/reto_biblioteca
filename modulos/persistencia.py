import json
import pickle
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
        try:
            with open("biblioteca.json", "w", encoding="utf-8") as f:
                json.dump(biblioteca.to_dict(), f, indent=4, ensure_ascii=False)

        except FileNotFoundError:
            print("El archivo no existe.")

        except PermissionError:
            print("No tienes permiso para leer este archivo.")

    def cargar(self):
        try:
            with open("biblioteca.json") as f:
                datos = json.load(f)

            return datos

        except FileNotFoundError:
            print("El archivo no existe.")

        except PermissionError:
            print("No tienes permiso para leer este archivo.")


class EstrategiaPickle(EstrategiaPersistencia):
    def guardar(self, biblioteca):
        try:
            with open("biblioteca.pkl", "wb") as f:
                pickle.dump(biblioteca.__dict__, f)

        except FileNotFoundError:
            print("El archivo no existe.")

        except PermissionError:
            print("No tienes permiso para leer este archivo.")

    def cargar(self):
        try:
            with open("biblioteca.pkl", "rb") as f:
                datos = pickle.load(f)

            return datos
        except FileNotFoundError:
            print("El archivo no existe.")

        except PermissionError:
            print("No tienes permiso para leer este archivo.")


if __name__ == '__main__':
    b = Biblioteca(['asa'], ["asa"], ["aaa"])
    e = EstrategiaJSON()
    # e.guardar(b)

    l, u, p = e.cargar()

    print(l)
    print(u)
    print(p)

    e2 = EstrategiaPickle()

    # e2.guardar(b)

    l2, u2, p2 = e.cargar()

    print(l2)
    print(u2)
    print(p2)
