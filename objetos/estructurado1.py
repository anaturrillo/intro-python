prendida = False
orden = ''
 
while orden != 'salir':
   orden = input("Introduzca orden: ")
   if orden == 'click':
       prendida = not prendida
   elif prendida == True:
       print(orden)
