def main():
    todas_las_notas = []

    while len(todas_las_notas) < 4:
        nota_recibida = int(input())
        
        if type(nota_recibida) != int:
            print('La nota tiene que se un numero')
        else: 
            nota = int(nota_recibida)
            if nota < 0 or nota > 10:
                print('La nota debe ser de 0 a 10')
            else:
                todas_las_notas.append(nota)

    sumatoria = 0

    for i in todas_las_notas:
        sumatoria += i

    promedio = sumatoria / len(todas_las_notas)

    print('el promedio /10 es ' + str(promedio))

main()





