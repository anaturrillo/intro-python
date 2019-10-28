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
            orden = self.pedir_orden()
            self.ejecutar_orden(orden)

    def pedir_orden(self):
        return input("Introduzca orden: ")

    def ejecutar_orden(self, orden):
        if orden == 'click':
            self.lapicera.click()
        else:
            self.lapicera.escribir(orden)

programa = Programa()
programa.iniciar()