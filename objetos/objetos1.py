class Lapicera:

    def __init__(self):
        self.prendida = False

    def click(self):
        self.prendida = not self.prendida
    
    def escribir(self, texto):
        if self.prendida:
            print(texto)

class Programa:

    def __init__(self):
        self.lapicera = Lapicera()

    def iniciar(self):
        orden = ''
        while orden != 'salir':
            orden = self.pedirOrden()
            self.ejecutarOrden(orden)

    def pedirOrden(self):
        return input("Introduzca orden: ")

    def ejecutarOrden(self, orden):
        if orden == 'click':
            self.lapicera.click()
        else:
            self.lapicera.escribir(orden)

programa = Programa()
programa.iniciar()