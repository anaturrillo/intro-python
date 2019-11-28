def calcular():
    a = 7
    def calculo(b):
        print(a + b)

    return calculo

miCalculo = calcular()
miCalculo(5)



