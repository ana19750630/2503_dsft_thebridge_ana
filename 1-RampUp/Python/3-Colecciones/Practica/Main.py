
##from funciones import * ##importame todas la funciones de funciones.py
from funciones import crear_tablero
from funciones import disparo
import pprint


tablero_computer = crear_tablero(10)
tablero_computer_visualizar = crear_tablero(10)

posicionar_barcos_fijos(tablero_computer)
print("tablero computer con barcos fijos")
print("tablero computer")
visualizar(tablero_computer)
print()

while True:
    print("Tus disparos")
    visualizar(tablero_computer_visualizar)
    print()
    i=int(input("introduce la fila, por favor:"))
    j=int(input("introduce la columna, por favor:"))
    acierto = disparo (tablero_computer,tablero_computer_visualizar,i,j)
    if not acierto:
        break
    os.system("cls")

pprint.pprint(tablero_computer)