import matplotlib.pyplot as plt
import Operaciones as Op
import math
import numpy as np

def Canicas(Matriz, X, Click, cont):
    for i in range (len(X)):
        for j in range(len(X)):
            if Matriz[i][j] != 1:
                if Matriz[i][j] != 0:
                    return print('Solo valores booleanos')

    if len(Matriz[0]) != len(X):
        return "No se puede realizar la operacion"
    else:
        mat = []
        for i in range(len(Matriz)):
            Sum = 0
            for j in range(len(Matriz)):
                mult = X[j] * Matriz[i][j]
                Sum = Sum + mult
            mat.append(Sum)
        if Click == cont:
            return print(mat)
        else:
            X = mat
            cont += 1
            Canicas(Matriz, X, Click, cont)

def RendijaProbabilistico(Matriz, X, Click, cont):
    sum = 0
    sum2 = 0
    for i in range(len(Matriz)):
        for j in range(len(X)):
            sum += Matriz[i][j]
            sum2 += Matriz[j][i]
    if sum == len(Matriz) and sum2 == len(Matriz):
        if len(Matriz[0]) != len(X):
            return "No se puede realizar la operacion"
        else:
            mat = []
            for i in range(len(Matriz)):
                Sum = 0
                for j in range(len(Matriz)):
                    mult = X[j] * Matriz[i][j]
                    Sum = Sum + mult
                mat.append(Sum)
            if Click == cont:
                fig = plt.figure()
                ax = fig.add_subplot(111)
                xx = range(len(mat))
                ax.bar(xx, mat)
                plt.xlabel('Estado')
                plt.ylabel('Porcetaje')
                plt.title('EvoluciÃ³n dinÃ¡mica del sistema despues de '+ str(Click) + ' Clicks de tiempo')
                plt.show()
                return mat
            else:
                X = mat
                cont += 1
                RendijaProbabilistico(Matriz, X, Click, cont)



def Cambio(Matriz, X, Click, cont):
     n = Matriz
     DobleRendija(Matriz, X, Click, cont, n)

def DobleRendija(Matriz, X, Click, cont, n):
    if cont == Click:
        S = Op.multiplicacionMatrizVector(n, X)
        Na = []
        for j in range(len(S)):
            Na.append(S[j][0])
        MATRIX = []
        for i in range(len(Na)):
            A = Op.modulo(Na[i])
            MATRIX.append(A)
        fig = plt.figure()
        ax = fig.add_subplot(111)
        xx = range(len(MATRIX))
        ax.bar(xx, MATRIX)
        plt.xlabel('Estado')
        plt.ylabel('Porcetaje')
        plt.title('Evolucion dinamica del sistema despues de '+ str(Click) + ' Clicks de tiempo')
        plt.show()
        return 
    else:
        n = Op.multiplicacionMatrizMatriz(n, Matriz)
        cont += 1
        DobleRendija(Matriz, X, Click, cont, n)
