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

sumatoria = 0

for i in todas_las_notas:
    sumatoria += i

promedio = sumatoria / len(todas_las_notas)

print('el promedio /10 es ' + str(promedio))

print('Quiere volver a ingresar las notas')
respuesta = input()

if respuesta == 'si':
    todas_las_notas_2 = []

    while len(todas_las_notas_2) < 4:
        nota_recibida_2 = input()
        
        if type(nota_recibida_2) != int:
            print('La nota tiene que se un numero')
        else: 
            nota_2 = int(nota_recibida_2)
            if nota_2 < 0 or nota_2 > 10:
                print('La nota debe ser de 0 a 10')
            else:
                todas_las_notas_2.append(nota_2)
    
    sumatoria_2 = 0

    for i in todas_las_notas_2:
        sumatoria_2 += i

    promedio_2 = sumatoria_2 / len(todas_las_notas_2)

    print('el promedio /10 es ' + str(promedio_2))
else:
    print('Gracias por usar promediator 3000')



