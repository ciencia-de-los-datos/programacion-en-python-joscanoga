"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""


def pregunta_01():
    file=open("data.csv")
    data=file.readlines()
    suma=0
    for i in data:
        suma += int(i.replace("\t"," ").split()[1])
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
    return suma


def pregunta_02():
    file = open("data.csv")
    data = file.readlines()
    diccionario={
        "A": 0,
        "B": 0,
        "C": 0,
        "D":0,
        "E":0
    }
    for i in data:
        aux=(i.replace("\t", " ").split()[0])
        diccionario[aux] += 1

    """
    Retorne la cantidad de registros por cada letra de la primera columna como la lista
    de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [
        ("A", 8),
        ("B", 7),
        ("C", 5),
        ("D", 6),
        ("E", 14),
    ]

    """
    return list(zip(diccionario.keys(),diccionario.values()))


def pregunta_03():
    file = open("data.csv")
    data = file.readlines()
    diccionario = {
        "A": 0,
        "B": 0,
        "C": 0,
        "D": 0,
        "E": 0
    }
    for i in data:
        fila=i.replace("\t", " ").split()
        letra = fila[0]
        numero= int(fila[1])
        diccionario[letra] += numero
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]

    """
    return list(zip(diccionario.keys(),diccionario.values()))


def pregunta_04():
    file = open("data.csv")
    data = file.readlines()
    diccionario = {
        "01": 0,
        "02": 0,
        "03": 0,
        "04": 0,
        "05": 0,
        "06": 0,
        "07": 0,
        "08": 0,
        "09": 0,
        "10": 0,
        "11": 0,
        "12": 0
    }
    for i in data:
        aux = (i.replace("\t", " ").split()[2].split("-")[1])
        diccionario[aux] += 1

    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
    registros por cada mes, tal como se muestra a continuación.

    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]

    """
    return list(zip(diccionario.keys(),diccionario.values()))

def pregunta_05():
    file = open("data.csv")
    data = file.readlines()
    max = {
        "A": -99999,
        "B": -99999,
        "C": -99999,
        "D": -99999,
        "E": -99999
    }
    min = {
        "A": 99999,
        "B": 99999,
        "C": 99999,
        "D": 99999,
        "E": 99999
    }
    for i in data:
        fila = i.replace("\t", " ").split()
        letra = fila[0]
        numero = int(fila[1])
        if max[letra]<numero:
            max[letra]=numero
        if min[letra]>numero:
            min[letra]=numero

    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
    letra de la columa 1.

    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]

    """
    return list(zip(min.keys(),max.values(),min.values()))



def pregunta_06():
    file = open("data.csv")
    data = file.readlines()
    max = {

    }
    min = {

    }
    for i in data:
        fila = i.replace("\t", " ").split()
        diccionarios=fila[4].split(",")
        for j in diccionarios:
            clave ,numero = j.split(":")
            if clave in min:
                if min[clave] > int(numero):
                    min[clave] = int(numero)
                elif max[clave] < int(numero):
                    max[clave] = int(numero)
            else:
                min[clave] = int(numero)
                max[clave] = int(numero)



    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.

    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]

    """
    lista=list(zip(min.keys(),min.values(),max.values()))
    lista.sort()
    return lista



def pregunta_07():
    file = open("data.csv")
    data = file.readlines()
    diccionario=dict()
    for i in data:
        fila = i.replace("\t", " ").split()
        clave=int(fila[1])
        valor=fila[0]
        if clave not in diccionario:
            diccionario[clave]=[]
        diccionario[clave].append(valor)


    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.

    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]

    """
    lista=list(zip(diccionario.keys(),diccionario.values()))
    lista.sort()
    return lista


def pregunta_08():
    file = open("data.csv")
    data = file.readlines()
    diccionario = dict()
    for i in data:
        fila = i.replace("\t", " ").split()
        clave = int(fila[1])
        valor = fila[0]
        if clave not in diccionario :
            diccionario[clave] = []
        if valor not in diccionario[clave]:
            diccionario[clave].append(valor)
        diccionario[clave].sort()

    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.

    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]

    """
    lista = list(zip(diccionario.keys(), diccionario.values()))
    lista.sort()
    return lista


def pregunta_09():
    file = open("data.csv")
    data = file.readlines()
    diccionario = {

    }

    for i in data:
        fila = i.replace("\t", " ").split()
        diccionarios = fila[4].split(",")
        for j in diccionarios:
            clave, numero = j.split(":")
            if clave not in diccionario:
                diccionario[clave]=1
            else:
                diccionario[clave] += 1

    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.

    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }

    """
    diccionario = dict(sorted(diccionario.items()))
    return diccionario


def pregunta_10():
    file = open("data.csv")
    data = file.readlines()
    letras=[]
    cantidades4=[]
    cantidades5 = []
    for i in data:
        fila = i.replace("\t", " ").split()
        letras.append(fila[0])
        cantidades4.append(len(fila[3].split(",")))
        cantidades5.append(len(fila[4].split(",")))

    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.

    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]


    """
    return list(zip(letras, cantidades4,cantidades5))


def pregunta_11():
    file = open("data.csv")
    data = file.readlines()
    diccionario = dict()
    for i in data:
        fila = i.replace("\t", " ").split()
        claves = fila[3].split(",")
        valor = int(fila[1])
        for j in claves:
            if j in diccionario:
                diccionario[j] += valor
            else:
                diccionario[j] = valor



    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.

    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }


    """
    diccionario = dict(sorted(diccionario.items()))
    return diccionario


def pregunta_12():
    file = open("data.csv")
    data = file.readlines()
    diccionario = {
        "A": 0,
        'B': 0,
        'C': 0,
        'D': 0,
        'E': 0
    }
    for i in data:
        fila = i.replace("\t", " ").split()
        clave = fila[0]
        valores= fila[4].split(",")
        suma=0
        for j in valores:
            suma += int(j.split(":")[1])
        diccionario[clave] += suma

    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }

    """
    return diccionario
