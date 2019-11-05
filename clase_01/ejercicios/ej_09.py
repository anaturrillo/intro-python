# 9) Escribir una funcion llamada estrellitas que imprima en consola el siguiente dibujo: 
# -
# --
# ---
# ----
# -----
# ------

def dibujar():
    for i in range(1, 7):
        print(i * '-')

dibujar()