from timeit import timeit
def bubble_sort(array):
    global cont
    cont = 0
    for i in range(len(array)):
        already_sorted = True
        for j in range(len(array)-i-1):
            cont += 1
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                already_sorted = False
        if already_sorted:
            break
    return array

array = bubble_sort([2,5,3,8,7,4,1,10,9,16,14,6,11,20,18])
print("Lista ordenada: ", array)
print("Tiempo segundos:", timeit())
print("Comparaciones:", cont)