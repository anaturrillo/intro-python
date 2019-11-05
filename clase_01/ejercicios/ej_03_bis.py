#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 3) Modificar la función anterior una vez más para que además el usuario pueda ingresar una operación y retornar el resultado de la operación (+, -, *, /)
# Solución alternativa

def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    return a / b        

operaciones = {
    "+": sumar,
    "-": restar,
    "*": multiplicar,
    "/": dividir
}

def operar():
    num_1 = input('Ingrese el primer número: ')
    operacion = input('Ingrese la operación: ')
    num_2 = input('Ingrese el siguiente número: ')
    
    num_1_int = int(num_1)
    num_2_int = int(num_2)
    
    return operaciones[operacion](num_1_int, num_2_int)

print( operar() )