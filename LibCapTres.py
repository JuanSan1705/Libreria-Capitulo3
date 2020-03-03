def Canicas(m, x, click, cont):
    if len(m[0]) != len(x):
        return "No se puede realizar la operación"
    else:
        mat = []
        for i in range(len(m)):
            Sum = 0
            for j in range(len(m)):
                mult = x[j] * m[i][j]
                Sum = Sum + mult
            mat.append(Sum)
        if click == cont:
            return mat
        else:
            x = mat
            cont += 1
            Canicas(m, x, click, cont)

def Cambio(m,x,NumRend,cont):
    n = m
    DobleRendija(m, x, NumRend, cont, n)

def DobleRendija(m, x, NumRend, cont, n):
    matriz = []
    if NumRend == 1:
        com = []
        for i in range(len(m)):
            Sum = 0
            for j in range(len(m)):
                mult = x[j] * m[i][j]
                Sum = Sum + mult
            com.append(Sum)
        return print(com)
    else:
        if NumRend == cont:
            mat = []
            for i in range(len(m)):
                Sum = 0
                for j in range(len(m)):
                    mult = x[j] * m[i][j]
                    Sum = Sum + mult
                mat.append(Sum)
            return print(mat)
        else:
            cont += 1
            for h in range(len(m)):
                matriz.append([0] * len(m))
            for i in range(len(m)):
                for j in range(len(m[0])):
                    for k in range(len(m)):
                        matriz[i][j] += m[i][k] * n[k][j]
            m = matriz
            DobleRendija(m, x, NumRend, cont, n)
