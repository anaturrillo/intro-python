
def ejecutar_orden(orden, estado_lapicera):
   if orden == 'click':
       estado_lapicera = not estado_lapicera
   elif estado_lapicera == True:
       print(orden)
   return estado_lapicera
 
def pedir_orden():
   return input("Introduzca orden: ")
 
 
esta_prendida = False
orden = ''
while orden != 'salir':
   orden = pedir_orden()
   esta_prendida = ejecutar_orden(orden, esta_prendida)
  
