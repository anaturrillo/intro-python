
def ejecutarOrden(orden, estadoLapicera):
   if orden == 'click':
       estadoLapicera = not estadoLapicera
   elif estadoLapicera == True:
       print(orden)
   return estadoLapicera
 
def pedirOrden():
   return input("Introduzca orden: ")
 
 
estaPrendida = False
orden = ''
while orden != 'salir':
   orden = pedirOrden()
   estaPrendida = ejecutarOrden(orden, estaPrendida)
  
