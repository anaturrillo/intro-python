
def notaEsInvalida(nota):
    if type(nota) != int:
        return 'La nota tiene que se un numero'
    
    notaInt = int(nota)
    if notaInt < 0 or notaInt > 10:
        return 'La nota debe ser de 0 a 10'

def solicitarNotas():
    todasLasNotas = []

    while len(todasLasNotas) < 4:
        notaRecibida = input()
        
        if notaEsInvalida(notaRecibida):
            print( notaEsInvalida(notaRecibida) )
        else:
            todasLasNotas.append(int(notaRecibida))
    return todasLasNotas

def main():
    notas = solicitarNotas()
    sumatoria = 0

    for i in notas:
        sumatoria += i

    promedio = sumatoria / len(notas)

    print('el promedio /10 es ' + str(promedio))

main()
