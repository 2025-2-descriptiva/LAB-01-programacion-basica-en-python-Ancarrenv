"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


## import the library
import csv
import os


## es una fucnion que puede llamar o hacer algo especifico, en este caso calcular y revolver una suma de la columna dos 

def pregunta_01():
    """
    Retorne la suma de la segunda columna.
    Rta/
    214
    """
    suma = 0 ## guardar la suma acomulada de todos los datos de la columna 2 
    with open('C:/Repositorios/LAB-01-programacion-basica-en-python-Ancarrenv-1/files/input/data.csv') as file: # abrir y como llamamaos el archivo
        for linea in file:  # vamos a correr linea para enocntrar la columna
            linea = linea.strip() 
            columnas = linea.split()
            
            valor = int(columnas[1])
            
            suma += valor       # Esto debe estar fuera del except, para que sume bien
    return suma              # Este return debe estar fuera del ciclo, para devolver el total al final

resultado = pregunta_01()
print(resultado)  
