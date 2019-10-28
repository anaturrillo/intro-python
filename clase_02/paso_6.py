
def nota_es_invalida(nota):
    if type(nota) != int:
        return 'La nota tiene que se un numero'
    
    nota_int = int(nota)
    if nota_int < 0 or nota_int > 10:
        return 'La nota debe ser de 0 a 10'

def solicitar_notas():
    todas_las_notas = []

    while len(todas_las_notas) < 4:
        nota_recibida = input()
        
        if nota_es_invalida(nota_recibida):
            print( nota_es_invalida(nota_recibida) )
        else:
            todas_las_notas.append(int(nota_recibida))
    return todas_las_notas

def calcular_promedio(notas):
    sumatoria = 0

    for i in notas:
        sumatoria += i

    return sumatoria / len(notas)

def imprimir_promedio(promedio):
    print('el promedio /10 es ' + str(promedio))

def main():
    notas = solicitar_notas()
    promedio = calcular_promedio(notas)

    imprimir_promedio(promedio)
    print('Quiere volver a ingresar las notas')
    respuesta = input()

    if respuesta == 'si':
        notas = solicitar_notas()
        promedio = calcular_promedio(notas)
        imprimir_promedio(promedio)
    else:
        print('Gracias por usar promediator 3000')


main()


