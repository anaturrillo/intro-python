# 4) Al ejercicio anterior agregarle la validación de la operacion

def operar():
    num_1 = input('Ingrese el primer número: ')
    operacion = input('Ingrese la operación: ')
    num_2 = input('Ingrese el siguiente número: ')
    
    num_1_int = int(num_1)
    num_2_int = int(num_2)

    if operacion == "+":
        return num_1_int + num_2_int
    
    elif operacion == "-":
        return num_1_int - num_2_int
    
    elif operacion == "*":
        return num_1_int * num_2_int
    
    elif operacion == "/":
        return num_1_int / num_2_int
    else:
        return 'La operacion es inválida'
        
print( operar() )