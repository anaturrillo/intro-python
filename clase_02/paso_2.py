def main():
    todasLasNotas = []

    while len(todasLasNotas) < 4:
        notaRecibida = int(input())
        
        if type(notaRecibida) != int:
            print('La nota tiene que se un numero')
        else: 
            nota = int(notaRecibida)
            if nota < 0 or nota > 10:
                print('La nota debe ser de 0 a 10')
            else:
                todasLasNotas.append(nota)

    sumatoria = 0

    for i in todasLasNotas:
        sumatoria += i

    promedio = sumatoria / len(todasLasNotas)

    print('el promedio /10 es ' + str(promedio))

main()





