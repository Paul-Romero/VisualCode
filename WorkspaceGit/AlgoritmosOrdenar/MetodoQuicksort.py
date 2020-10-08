from random import randint
from timeit import timeit

def quicksort(array):
    global cont
    if len(array) < 2:
        return array
    low, same, high = [], [], []
    pivot = array[randint(0, len(array) - 1)]
    cont = 0
    for item in array:
        cont += 1
        if item < pivot:
            low.append(item)
        elif item == pivot:
            same.append(item)
        elif item > pivot:
            high.append(item)
    return quicksort(low) + same + quicksort(high)

array = quicksort([2,5,3,8,7,4,1,10,9,16,14,6,11,20,18])
print("Lista ordenada: ", array)
print("Tiempo segundos:", timeit())
print("Comparaciones:", cont)