import random
import timeit
from turtle import left

datos = [random.randint(1, 100) for _ in range(20)]

print("Lista sin ordenar:", datos)


lista = datos.copy()

def mergeSort(arr):
    if len(arr) <= 1:
        return arr
        
    mid = len(arr) // 2
    leftHalf = arr[:mid]
    rightHalf = arr[mid:]
        
    leftHalf = mergeSort(leftHalf)
    rightHalf = mergeSort(rightHalf)

    i = j = 0
    resultado = []

    while i < len(leftHalf) or j < len(rightHalf):
        if i >= len(leftHalf) or j >= len(rightHalf):
            if i < len(leftHalf):
                resultado.append(leftHalf[i])
                i += 1
                continue
            else:
                resultado.append(rightHalf[j])
                j += 1
                continue

        if leftHalf[i] < rightHalf[j]:
            resultado.append(leftHalf[i])
            i += 1
        else:
            resultado.append(rightHalf[j])
            j += 1

    return resultado

print("Lista ordenada>: ")
print(mergeSort(lista))
tiempo10 = timeit.timeit(lambda: mergeSort(lista), number=10)
print("Tiempo de ejecución:", tiempo10, "segundos") 
tiempo100 = timeit.timeit(lambda: mergeSort(lista), number=100)
print("Tiempo de ejecución:", tiempo100, "segundos")
tiempo1000 = timeit.timeit(lambda: mergeSort(lista), number=1000)
print("Tiempo de ejecución:", tiempo1000, "segundos")
