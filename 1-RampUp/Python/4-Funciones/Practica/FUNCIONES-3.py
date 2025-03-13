
def modificar_lista(lista, comando, elemento=None):
    if comando == "add":
        if elemento is not None:
            lista.append(elemento)
    elif comando == "remove":
        if elemento is not None and elemento in lista:
            lista.remove(elemento)
    return lista

# Ejemplo de uso:
mi_lista = [1, 2, 3]

# Añadir un elemento
mi_lista = modificar_lista(mi_lista, "add", 4)
print(mi_lista)  # Salida: [1, 2, 3, 4]

# Eliminar un elemento
mi_lista = modificar_lista(mi_lista, "remove", 2)
print(mi_lista)  # Salida: [1, 3, 4]
