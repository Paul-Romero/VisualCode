from timeit import timeit

def merge(left, right):
    global cont
    if len(left) == 0:
        return right
    if len(right) == 0:
        return left
    result = []
    index_left = index_right = cont = 0
    while len(result) < len(left) + len(right):
        cont += 1
        if left[index_left] <= right[index_right]:
            result.append(left[index_left])
            index_left += 1
        else:
            result.append(right[index_right])
            index_right += 1
        if index_right == len(right):
            result += left[index_left:]
            break
        if index_left == len(left):
            result += right[index_right:]
            break
    return result

def merge_sort(array):
    if len(array) < 2:
        return array
    midpoint = len(array)//2
    return merge(left=merge_sort(array[:midpoint]),
        right=merge_sort(array[midpoint:]))

array = merge_sort([2,5,3,8,7,4,1,10,9,16,14,6,11,20,18])
print("Lista ordenada: ", array)
print("Tiempo segundos:", timeit())
print("Comparaciones:", cont)