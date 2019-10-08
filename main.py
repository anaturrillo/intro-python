#!/usr/bin/env python
# -*- coding: utf-8 -*-

def esNotaInvalida(nota):
    if type(nota) != int:
        return {'error': 'La nota tiene que se un numero'}

    notaInt = int(nota)
    if notaInt < 0 or notaInt > 10:
        return {'error': 'La nota debe ser de 0 a 10'}
    
    return {'success': notaInt}

def recibirNotas():
    todasLasNotas = []

    while len(todasLasNotas) < 4:
        notaRecibida = input()
        notaValidada = esNotaInvalida(notaRecibida) 
        
        if 'error' in notaValidada:
            print( notaValidada['error'] )
        else:
            todasLasNotas.append(notaValidada['success'])

    return todasLasNotas



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
        notaRecibida = input()
        notaValidada = esNotaInvalida(notaRecibida)
        if 'error' in notaValidada:
            print( notaValidada['error'] )
            return recibirNotas_(notas)
        else:
            return recibirNotas_([notaValidada['success']] + notas)