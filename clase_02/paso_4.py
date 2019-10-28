
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

def main():
    notas = solicitar_notas()
    sumatoria = 0

    for i in notas:
        sumatoria += i

    promedio = sumatoria / len(notas)

    print('el promedio /10 es ' + str(promedio))

main()
