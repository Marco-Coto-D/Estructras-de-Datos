import random
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
