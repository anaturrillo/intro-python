def solicitar_notas():
    todas_las_notas = []

    while len(todas_las_notas) < 4:
        nota_recibida = input()
        
        if type(nota_recibida) != int:
            print('La nota tiene que se un numero')
        else: 
            nota = int(nota_recibida)
            if nota < 0 or nota > 10:
                print('La nota debe ser de 0 a 10')
            else:
                todas_las_notas.append(nota)
    return todas_las_notas

def main():
    notas = solicitar_notas()
    sumatoria = 0

    for i in notas:
        sumatoria += i

    promedio = sumatoria / len(notas)

    promedioSobre10 = promedio
    promedioSobre100 = promedio * 10
    promedioSobre50 = promedio * 5

    print('el promedio /10 es ' + str(promedioSobre10))

main()

