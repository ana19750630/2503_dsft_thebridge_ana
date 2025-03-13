

# Creación de un tablero 10x10 con espacios vacíos representados por el carácter " "
tablero = [[" " for _ in range(10)] for _ in range(10)]

# Imprimir el tablero
##for fila in tablero:
    ##print(fila)
##print()

# Insertar el barco de 4 casillas en horizontal en las posiciones [1][0], [1][1], [1][2], [1][3]
## [fila] [columna]
tablero[1][0] = "B"
tablero[1][1] = "B"
tablero[1][2] = "B"
tablero[1][3] = "B"

# Insertar el barco de 3 casillas en vertical en las posiciones [3][3], [4][3], [4][4], [4][5]
tablero[4][2] = "B"
tablero[4][3] = "B"
tablero[4][4] = "B"
tablero[4][5] = "B"

# Imprimir el tablero con los barcos
for fila in tablero:
    print(fila)


##funcion para disparar en el tablero.
def disparo(tablero,i,j):
    if tablero[i][j] =='B':
        print("Tocado")
        print("Sigue jugando")
        tablero[i][j]= "x"
        print(tablero)
        return True

    else: tablero[i][j] == ""
    print("agua")
    tablero[i][j] = "0"
    print(tablero)
    return True

while True:
    i = int(input("introduce la fila"))
    j = int(input("introduce la columna"))
    if not disparo(tablero,i,j):
        break