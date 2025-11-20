"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


### nota los diccionarios y las listas son mutables o cmabiantes, las tuplas y las cadenas no 

def pregunta_02():

    conteo = {} ## se crea un diccionario porque se desea asociar la letra al conteo, ya que es clave y valor, es rapido y se actualiza facilmente, las tupla sno cmabia, no se puede sumar y agregar algo
    """
    Retorne la cantidad de registros por cada letra de la primera columna como
    la lista de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [('A', 8), ('B', 7), ('C', 5), ('D', 6), ('E', 14)]

    """
    with open('C:/Repositorios/LAB-01-programacion-basica-en-python-Ancarrenv-1/files/input/data.csv') as file: # abrir y como llamamaos el archivo
        for linea in file:  # vamos a correr linea para enocntrar la columna
            linea = linea.strip() 
            columnas = linea.split('\t')

            letras = columnas[0]

            if letras in conteo:
                conteo[letras] += 1
            else:
                conteo[letras] = 1
                
    list_tuplas =  list(conteo.items()) ## convierte el dic en una lista de tuplas
    list_tuplas.sort(key=lambda x: x[0]) # ordena
    return list_tuplas    

resultado = pregunta_02()
print(resultado)