#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 2) Modificar la función anterior para que pida los valores por input

def sumar():
    num_1 = input('Ingrese el primer número: ')
    num_2 = input('Ingrese el siguiente número: ')
    
    num_1_int = int(num_1)
    num_2_int = int(num_2)

    return num_1_int + num_2_int

print( sumar() )