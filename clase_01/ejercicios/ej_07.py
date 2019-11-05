# 7) Crear una función que reciba un array de números y devuelva el mayor
def encontrar_el_mayor(numeros):
    mayor = numeros[0]
    
    for numero in numeros:
        if numero > mayor:
            mayor = numero
    
    return mayor

print( encontrar_el_mayor( [10, 4, 2, 6] ) )
print( encontrar_el_mayor( [1, 2, 3, 5] ) )
print( encontrar_el_mayor( [5, 10, 20, 30, 5, 2] ) )