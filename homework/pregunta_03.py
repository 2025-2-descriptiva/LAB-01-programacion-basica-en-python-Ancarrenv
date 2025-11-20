"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como
    una lista de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [('A', 53), ('B', 36), ('C', 27), ('D', 31), ('E', 67)]

    """
    letras = []
    numeros = []

    with open(r"files/input/data.csv", "r", encoding="utf-8") as data:
        for linea in data:
            lista = linea.strip().split("\t")
            letras.append(lista[0])   
            numeros.append(int(lista[1]))

    resultado = {}
    for letra_unica in set(letras):
        suma = 0
        for i in range(len(letras)):
            if letras[i] == letra_unica:
                suma += numeros[i]
        resultado[letra_unica] = suma
    
    resultado = sorted(resultado.items())
    
    return resultado

# resultado = pregunta_03()
# print(resultado)

if __name__ == "__main__":
    print(pregunta_03())