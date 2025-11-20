"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_04():
    conteo = {}

    """
    
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la
    cantidad de registros por cada mes, tal como se muestra a continuación.

    Rta/
    [('01', 3),
     ('02', 4),
     ('03', 2),
     ('04', 4),
     ('05', 3),
     ('06', 3),
     ('07', 5),
     ('08', 6),
     ('09', 3),
     ('10', 2),
     ('11', 2),
     ('12', 3)]

    """
    with open('C:/Repositorios/LAB-01-programacion-basica-en-python-Ancarrenv-1/files/input/data.csv') as file :
        for linea in file:
            linea = linea.strip()
            columna = linea.split('\t')

            date_str = columna[2]
            fecha_mes = (date_str.split('-')[1]).zfill(2)
        

            if  fecha_mes  in conteo:
                conteo[fecha_mes] += 1
            else:
                conteo[fecha_mes] = 1

    list_tuplas =  list(conteo.items()) ## convierte el dic en una lista de tuplas
    list_tuplas.sort(key=lambda x: x[0]) # ordena
    return list_tuplas   

resultado = pregunta_04()
print(resultado)
