from datetime import *


def input_str(data, min_len=1, max_len=None):
    """
    Input personalizado para validar que se cumplen las condiciones pertinentes del tipo str

    Parameters:
    data (str): Texto que se muestra en el input
    min_len (int): Número minimo de caracteres que se deben introducir
    max_len (int): Número maximo de caracteres que se deben introducir

    Returns:
    str: Entrada introducida por el usuario validada
    """
    try:
        value = input(data)
        if len(value) < min_len:
            raise ValueError(f'Debe tener por lo menos {min_len} caracter(es)')
        if max_len is not None and len(value) > max_len:
            raise ValueError(f'No debe tener mas de {min_len} caracter(es)')
        return value
    except ValueError as e:
        print('La entrada insertada tuvo un error de longitud:', e)
        return input_str(data, min_len, max_len)


def input_base(type_func, data, min_data, max_data):
    """
    Input base que comprueba tanto el tipo de dato pertinente como si cumple un rango con un minimo y un maximo

    Parameters:
    type_func (int/float): Tipo de dato numérico a comprobar
    data (str): Texto que se muestra en el input
    min_data (int): Número minimo que se deben introducir
    max_data (int): Número maximo que se deben introducir

    Returns:
    int/float: Entrada introducida por el usuario validada
    """
    try:
        value = type_func(input_str(data))
        if min_data is not None and value < min_data:
            raise ValueError(f'El numero debe ser mayor o igual que {min_data}')
        if max_data is not None and value > max_data:
            raise ValueError(f'El numero debe ser menor o igual que {max_data}')
        return value
    except ValueError as e:
        print(f'El valor ingresado no es valido, debe ser un numero {type_func.__name__}:', e)
        return input_base(type_func, data, min_data, max_data)


def input_int(data, min_data=None, max_data=None):
    """
    Input personalizado para validar que se cumplen las condiciones pertinentes del tipo int

    Parameters:
    data (str): Texto que se muestra en el input
    min_data (int): Número minimo que se deben introducir
    max_data (int): Número maximo que se deben introducir

    Returns:
    int: Entrada introducida por el usuario validada
    """
    return input_base(int, data, min_data, max_data)


def input_float(data, min_data=None, max_data=None):
    """
    Input personalizado para validar que se cumplen las condiciones pertinentes del tipo float

    Parameters:
    data (str): Texto que se muestra en el input
    min_data (int): Número minimo que se deben introducir
    max_data (int): Número maximo que se deben introducir

    Returns:
    float: Entrada introducida por el usuario validada
    """
    return input_base(float, data, min_data, max_data)


def input_date(data):
    """
    Input personalizado para validar que se cumplen las condiciones pertinentes del tipo datetime

    Parameters:
    data (str): Texto que se muestra en el input

    Returns:
    datetime: Entrada introducida por el usuario validada
    """
    try:
        value = input_str(data)
        year, month, day = value.split('-')
        new_year = datetime(int(year), int(month), int(day))
        return new_year
    except ValueError as e:
        print(f'La fecha ingresada no es valida, debe seguir este formato "2025-03-27":', e)
        return input_date(data)
