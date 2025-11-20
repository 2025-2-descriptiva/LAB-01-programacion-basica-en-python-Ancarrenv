"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor
    la suma de los valores de la columna 5 sobre todo el archivo.

    Rta/
    {'A': 177, 'B': 187, 'C': 114, 'D': 136, 'E': 324}
    """
    resultado = {}

    with open('C:/Repositorios/LAB-01-programacion-basica-en-python-Ancarrenv-1/files/input/data.csv') as file:
        for linea in file:
            linea = linea.strip()
            columnas = linea.split('\t')

            clave = columnas[0]            # Columna 1
            column_spli = columnas[4].split(',')       # Columna 5 

            suma = 0
            for par in column_spli:
                _, valor = par.split(':')   # separa la clave y el número
                suma += int(valor)

            if clave in resultado:
                resultado[clave] += suma
            else:
                resultado[clave] = suma
            
            
    return dict(sorted(resultado.items()))

print(pregunta_12())
