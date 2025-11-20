"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_03():
    conteo = {}
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como
    una lista de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [('A', 53), ('B', 36), ('C', 27), ('D', 31), ('E', 67)]

    """
    with  open('C:/Repositorios/LAB-01-programacion-basica-en-python-Ancarrenv-1/files/input/data.csv') as file: # abrir y como llamamaos el archivo
        for linea in file:
            linea = linea.strip()
            columnas= linea.split('\t')

            letras = columnas[0]
            valor = int(columnas[1])
          
            if letras in conteo:
                conteo[letras] += valor
            else:
                conteo[letras] = valor

    list_tuplas =  list(conteo.items()) ## convierte el dic en una lista de tuplas
    list_tuplas.sort(key=lambda x: x[0]) # ordena
    return list_tuplas  

resultado = pregunta_03()
print(resultado)