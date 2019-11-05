# 10) Escribir una función que reciba un numero y valide si el número es primo. La funcion debe retornar una mensaje

def chequear_primo(num):
    es_primo = True

    for i in range(2, num):        
        if num % i == 0:
            es_primo = False
        

    if es_primo:
        return 'El número es primo'
    else:
        return 'El numero no es primo'



print( chequear_primo(10) )
print( chequear_primo(14) )
print( chequear_primo(13) )
print( chequear_primo(217) )