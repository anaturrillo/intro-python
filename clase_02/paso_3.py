def solicitarNotas():
    todasLasNotas = []

    while len(todasLasNotas) < 4:
        notaRecibida = input()
        
        if type(notaRecibida) != int:
            print('La nota tiene que se un numero')
        else: 
            nota = int(notaRecibida)
            if nota < 0 or nota > 10:
                print('La nota debe ser de 0 a 10')
            else:
                todasLasNotas.append(nota)
    return todasLasNotas

def main():
    notas = solicitarNotas()
    sumatoria = 0

    for i in notas:
        sumatoria += i

    promedio = sumatoria / len(notas)

    promedioSobre10 = promedio
    promedioSobre100 = promedio * 10
    promedioSobre50 = promedio * 5

    print('el promedio /10 es ' + str(promedioSobre10))

main()

