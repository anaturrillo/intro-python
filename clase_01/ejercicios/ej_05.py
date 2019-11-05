# 5) Crear una función que reciba dos numeros y devuelva el mayor

def dame_el_mayor(a, b):
    int_a = int(a)
    int_b = int(b)

    if int_a >= int_b:
        return int_a
    else:
        return int_b

print(dame_el_mayor(10, 5))
print(dame_el_mayor(2, 5))