"""
-Para pbtener el numero de iteraciones de un ciclo de ir sacando 0s, es n*n-n
-El pivote siempre será col,col, solo q a veces estará arriba o abajo
"""

#------------------------------------------------------BIBLIOTECAS--------------------------------------------------------
import re



#------------------------------------------------------FUNCIONES--------------------------------------------------------

def imprimirMatriz(matriz):
    for eq in matriz:
        print(eq)


#arreglo1[]=multiplocarRenglon(matriz[col]("este es el renglon pivote"), matriz[ren][col]("valor a poner en 0"))
#arreglo2[]=multiplocarRenglon(matriz[ren]("este es el renglon del valor a poner en 0"), matriz[col][col]("valor pivote"))
def multiplicarRenglon(arreglo, valor):
    for i in len(arreglo):
        arreglo[i]= arreglo[i]*valor
    return arreglo


#resultado[]=restarArreglos(arrelos1, arreglo2)("arreglo1-arreglo2")
def restarArreglos(arreglo1, arreglo2):
    resultado=[]
    for i in len(arreglo1):
        resultado[i] = arreglo1[i] - arreglo2[i]
    return resultado


#matriz=insertarRenglonResultado(matriz[][], resultado[], ren, col)
def insertarRenglonResultado(matriz, renglon, ren):
    for i in len(renglon):
        matriz[ren][i] = renglon[i]
    #no regreso nada xq ya se pasa x referencia la matriz, y tampoco ocupo la variable col


def resolverGaussJordan(matriz, numVariables):

    for ren in range(0,numVariables):
        for col in range(0, numVariables):

            if ren == col:
                break

            #imprimo la iteracion de la matriz
            imprimirMatriz(matriz)

            #arreglo1[]=multiplocarRenglon(matriz[col]("este es el renglon pivote"), matriz[ren][col]("valor a poner en 0"))
            arreglo1 = multiplicarRenglon(matriz[col], matriz[ren][col])
            #arreglo2[]=multiplocarRenglon(matriz[ren]("este es el renglon del valor a poner en 0"), matriz[col][col]("valor pivote"))
            arreglo2 = multiplicarRenglon(matriz[ren], matriz[col][col])
            #resultado[]=restarArreglos(arrelos1, arreglo2)("arreglo1-arreglo2")
            resultado = restarArreglos(arreglo1, arreglo2)
            #matriz=insertarRenglonResultado(matriz[][], resultado[], ren, col)
            insertarRenglonResultado(matriz, resultado, ren)



#----------------------------------------------------EL MAIN------------------------------------------------------------


#           Primero abro y leo el archivo
f= open("entrada.txt", "r")
txt = f.read()
f.close()


#             Creo la matriz del sistema de ecuaciones
matriz = []

for ren in txt.split('\n'):
    if len(ren) ==0:
        break
    # arr = ren.split(' ')
    # m = map(float, arr)
    # eq = list(m)

    # Separa el lado izquierdo y derecho de la ecuación
    left, right = ren.split('=')
    # Separa el lado izquierdo por las variables
    # No utiliza el último elemento porque por alguna razón queda vacío
    # Después adjuntael lado izquierdo de la ecuación
    matriz +=[list(map(float, re.split(r'[a-z]', left[0:-1])))+[float(right)]]


#             Imprimo la matriz para corroborar que está bien escrita

#for eq in matriz:
#    print(eq)

#           Encuentro el tamaño de la matriz
numVariables = len(matriz[0]) -1

#           Mando llamar a la función que empezará a resolver todo
resolverGaussJordan(matriz, numVariables)
