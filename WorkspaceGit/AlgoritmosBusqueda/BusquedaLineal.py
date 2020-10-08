def BusquedaLineal(lista, n):
    for i in lista:
        if n == i:
            return("Encontrado! ", n, "Posición: ", lista.index(n))
    return("El elemento no se encuentró.")