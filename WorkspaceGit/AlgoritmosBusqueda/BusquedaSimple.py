def BusquedaSimplex(lista, n):
    if n in lista:
        return("Encontrado! ", n, "Posición: ", lista.index(n))
    else:
        raise Warning("El elemento no se encuentró.")