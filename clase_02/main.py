#!/usr/bin/env python
# -*- coding: utf-8 -*-

def esNotaInvalida(nota):
    if type(nota) != int:
        return {'error': 'La nota tiene que se un numero'}

    nota_int = int(nota)
    if nota_int < 0 or nota_int > 10:
        return {'error': 'La nota debe ser de 0 a 10'}
    
    return {'success': nota_int}

def recibirNotas():
    todas_las_notas = []

    while len(todas_las_notas) < 4:
        nota_recibida = input()
        notaValidada = esNotaInvalida(nota_recibida) 
        
        if 'error' in notaValidada:
            print( notaValidada['error'] )
        else:
            todas_las_notas.append(notaValidada['success'])

    return todas_las_notas



def main():
    notas = recibirNotas()

    sumatoria = 0

    for i in notas:
        sumatoria += i

    promedio = sumatoria / len(notas)

    promedioSobre10 = promedio
    promedioSobre100 = promedio * 10
    promedioSobre50 = promedio * 5

    print('el promedio /10 es')
    print(promedioSobre10)

main() 


# para recursividad

def recibirNotas_(notas):
    if len(notas) == 4:
        return notas
    else:
        nota_recibida = input()
        notaValidada = esNotaInvalida(nota_recibida)
        if 'error' in notaValidada:
            print( notaValidada['error'] )
            return recibirNotas_(notas)
        else:
            return recibirNotas_([notaValidada['success']] + notas)