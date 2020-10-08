def BusquedaBinaria(lista, n):
    liminf, limsup = 0, len(lista) - 1
    while liminf <= limsup:
        med = (liminf+limsup)//2
        if lista[med] == n:
            return("Encontrado! ", n, "Posición: ", lista.index(n))
        elif lista[med] > n:
            limsup = med - 1
        else:
            liminf = med + 1
    return("El elemento no se encuentró.")