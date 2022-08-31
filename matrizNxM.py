'''
Fuente: https://www.youtube.com/watch?v=tq8XsNjkyec&t=152s&ab_channel=ManuelGonz%C3%A1lez
name: Manuel Gonzales
channel: YouTube CL
'''
#!Note: La matriz generada debes guardarla en un archivo de texto plano con el nombre "matriz_n_por_m.txt"

import random;

def llenarMatriz(row, column):
    matriz = [];

    # range (inicio. final, intervalo (de cuanto va a incrementar))
    # range (inicio, final)
    # range (cantidad_total_de_iteraciones)
    for i in range(row):
        # ? Sera que al recorrer con la primera iteración, le estamos asignando el tamaño de la matriz
        matriz.append([]);
        for j in range(column):
            numeros = random.randint(0, 20);
            matriz[i].append(numeros);

    return matriz;

def imprimirMatriz(matriz):
    # Mostramos la matriz, utilizado un forEach
    for fila in matriz:
        print("", end="");

        for valores in fila:
            print(valores, end="\t");
        print("");