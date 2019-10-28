def saludo():
    nombre = 'Manola'
    def texto():
        return 'Hola ' + nombre + '!'
    return texto

saludar = saludo()

print( saludar )
print( saludar() )
