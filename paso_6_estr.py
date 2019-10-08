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

sumatoria = 0

for i in todasLasNotas:
    sumatoria += i

promedio = sumatoria / len(todasLasNotas)

print('el promedio /10 es ' + str(promedio))

print('Quiere volver a ingresar las notas')
respuesta = input()

if respuesta == 'si':
    todasLasNotas_2 = []

    while len(todasLasNotas_2) < 4:
        notaRecibida_2 = input()
        
        if type(notaRecibida_2) != int:
            print('La nota tiene que se un numero')
        else: 
            nota_2 = int(notaRecibida_2)
            if nota_2 < 0 or nota_2 > 10:
                print('La nota debe ser de 0 a 10')
            else:
                todasLasNotas_2.append(nota_2)
    
    sumatoria_2 = 0

    for i in todasLasNotas_2:
        sumatoria_2 += i

    promedio_2 = sumatoria_2 / len(todasLasNotas_2)

    print('el promedio /10 es ' + str(promedio_2))
else:
    print('Gracias por usar promediator 3000')



