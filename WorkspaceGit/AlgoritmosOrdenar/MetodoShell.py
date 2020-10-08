from timeit import timeit

def shell_sort(array):
    global cont
    cont = 0
    g = len(array) / 2
    while int(g) > 0:
        for i in range(int(g), len(array)):
            value = array[i]
            j = i
            cont += 1
            while j >= int(g) and array[j-int(g)] > value:
                array[j] = array[j-int(g)]
                j -= int(g)
            array[j] = value
        g /= 2
    return array

array = shell_sort([2,5,3,8,7,4,1,10,9,16,14,6,11,20,18])
print("Lista ordenada: ", array)
print("Tiempo segundos:", timeit())
print("Comparaciones:", cont)
