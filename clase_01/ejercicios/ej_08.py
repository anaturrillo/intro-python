# 8) Crear una función que sume todos los números entre 0 y 1000

def sumar():
    suma = 0

    for i in range(0, 1001):
        suma = suma + i

    return suma

print( sumar() )