from timeit import timeit

def insertion_sort(array):
    global cont
    cont = 0
    for i in range(1, len(array)):
        key_item = array[i]
        j = i - 1
        while j >= 0 and array[j] > key_item:
            cont += 1
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key_item
    return array

array = insertion_sort([2,5,3,8,7,4,1,10,9,16,14,6,11,20,18])
print("Lista ordenada: ", array)
print("Tiempo segundos:", timeit())
print("Comparaciones:", cont)