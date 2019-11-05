# 6) Escribir una función llamada fizz_buzz que reciba un numero y devuelva fizz si el numero es divisible por 3, buzz si es divisible por 5 y FizzBuzz si es divisible por ambos

def fizz_buzz(num):
    if num % 5 == 0 and num % 3 == 0:
        return 'FizzBuzz'
    elif num % 3 == 0:
        return 'buzz'
    else:
        return 'fizz'

print( fizz_buzz(9) )
print( fizz_buzz(5) )
print( fizz_buzz(15) )
print( fizz_buzz(28) )