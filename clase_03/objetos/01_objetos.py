class Gato:
    def __init__(self, color):
        self.color = color

    def caminar(self):
        print('estoy caminando')

gato_gris = Gato('gris')
gato_gris.caminar()
print(gato_gris.color)
